# AGENTS.md

## Tech Stack

- Jekyll 4.x (Ruby-based) static site generator with al-folio theme
- Docker-based development environment
- Prettier (via npm) for formatting HTML/Liquid files

## Commands

```bash
npm run dev           # Start local preview on http://localhost:8080 (runs docker compose up)
npm run build         # Build site without starting server
npm run install-gems  # Install Ruby dependencies
npm run format        # Format all files with Prettier
npm run format:check  # Check formatting without modifying
```

## Key Conventions

- **Docker is required** for local development (no native Ruby required)
- **Prettier format checks run on push** via GitHub Actions (`.github/workflows/prettier.yml`)
- **Deploy on push** via `.github/workflows/deploy.yml`
- Site source in root; `_site/` is generated output (gitignored)

## Directory Structure

- `_pages/` — website pages (Markdown with frontmatter)
- `_posts/` — blog posts
- `_projects/`, `_news/`, `_books/` — Jekyll collections
- `_bibliography/` — BibTeX files for publications
- `_data/` — YAML config (cv.yml, repositories.yml, socials.yml)
- `_layouts/`, `_includes/` — Liquid templates

## Agent Instructions

- `.github/agents/docs.agent.md` — specialized agent for documentation updates
- Read existing agent instructions before modifying source files
