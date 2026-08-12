#!/usr/bin/env python
"""Sync the `github_repos` list in `_data/repositories.yml` with the repos
currently pinned on a GitHub profile.

GitHub does not expose pinned-repo status via the public REST API -- it is
only available through the GraphQL API (`user.pinnedItems`), which always
requires an authenticated request, even for public data. In GitHub Actions
the default `secrets.GITHUB_TOKEN` is sufficient (it only needs to read
public data). For local runs, export a `GITHUB_TOKEN` (or `GH_TOKEN`)
environment variable set to a PAT with no special scopes (e.g. one created
with no boxes checked works fine for reading public pinned items).
"""

import os
import sys

import requests
import yaml

GITHUB_GRAPHQL_URL = "https://api.github.com/graphql"
SOCIALS_FILE = "_data/socials.yml"
OUTPUT_FILE = "_data/repositories.yml"

PINNED_ITEMS_QUERY = """
query($login: String!) {
  user(login: $login) {
    pinnedItems(first: 6, types: [REPOSITORY]) {
      nodes {
        ... on Repository {
          nameWithOwner
        }
      }
    }
  }
}
"""


def load_github_username() -> str:
    """Load the GitHub username whose pinned repos should be mirrored."""
    if not os.path.exists(SOCIALS_FILE):
        print(
            f"Configuration file {SOCIALS_FILE} not found. Please ensure the file exists and contains your GitHub username."
        )
        sys.exit(1)
    try:
        with open(SOCIALS_FILE, "r") as f:
            config = yaml.safe_load(f) or {}
        github_username = config.get("github_username")
        if not github_username:
            print(
                f"No 'github_username' found in {SOCIALS_FILE}. Please add 'github_username' to _data/socials.yml."
            )
            sys.exit(1)
        return github_username
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file {SOCIALS_FILE}: {e}. Please check the file for correct YAML syntax.")
        sys.exit(1)


def load_github_token() -> str:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        print(
            "No GITHUB_TOKEN or GH_TOKEN environment variable set. The GraphQL "
            "pinnedItems query requires an authenticated request even for public "
            "data. In GitHub Actions this is provided automatically via "
            "secrets.GITHUB_TOKEN; for local runs, export a PAT with no special "
            "scopes."
        )
        sys.exit(1)
    return token


def fetch_pinned_repos(username: str, token: str) -> list:
    """Fetch the list of `owner/repo` names currently pinned on a profile."""
    print(f"Fetching pinned repositories for GitHub user: {username}")
    try:
        response = requests.post(
            GITHUB_GRAPHQL_URL,
            json={"query": PINNED_ITEMS_QUERY, "variables": {"login": username}},
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github+json",
            },
            timeout=15,
        )
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error querying the GitHub GraphQL API for user '{username}': {e}")
        sys.exit(1)

    payload = response.json()
    if "errors" in payload:
        print(f"GitHub GraphQL API returned errors: {payload['errors']}")
        sys.exit(1)

    user = (payload.get("data") or {}).get("user")
    if not user:
        print(f"No such GitHub user: '{username}'. Please check 'github_username' in {SOCIALS_FILE}.")
        sys.exit(1)

    nodes = user.get("pinnedItems", {}).get("nodes", [])
    pinned_repos = [node["nameWithOwner"] for node in nodes if node]

    for repo in pinned_repos:
        print(f"Found pinned repo: {repo}")

    return pinned_repos


def update_repositories_yaml(pinned_repos: list) -> None:
    """Rewrite `github_repos` in _data/repositories.yml, preserving other keys."""
    if not os.path.exists(OUTPUT_FILE):
        print(f"Configuration file {OUTPUT_FILE} not found. Please ensure the file exists.")
        sys.exit(1)

    with open(OUTPUT_FILE, "r") as f:
        data = yaml.safe_load(f) or {}

    if data.get("github_repos") == pinned_repos:
        print("No changes in pinned repositories. Skipping file update.")
        return

    print("Pinned repositories changed:")
    print(f"  before: {data.get('github_repos')}")
    print(f"  after:  {pinned_repos}")

    data["github_repos"] = pinned_repos

    try:
        with open(OUTPUT_FILE, "w") as f:
            yaml.dump(data, f, sort_keys=False, default_flow_style=False, width=1000)
        print(f"Updated {OUTPUT_FILE}")
    except Exception as e:
        print(f"Error writing to {OUTPUT_FILE}: {e}. Please check file permissions and disk space.")
        sys.exit(1)


def main() -> None:
    username = load_github_username()
    token = load_github_token()
    pinned_repos = fetch_pinned_repos(username, token)
    if not pinned_repos:
        print("No pinned repositories found for this user. Leaving the file unchanged.")
        return
    update_repositories_yaml(pinned_repos)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
