# Santiago Casas

[![Deploy](https://github.com/santiagocasas/santiagocasas.github.io/actions/workflows/deploy.yml/badge.svg)](https://github.com/santiagocasas/santiagocasas.github.io/actions/workflows/deploy.yml)
[![Code Style](https://github.com/santiagocasas/santiagocasas.github.io/actions/workflows/prettier.yml/badge.svg)](https://github.com/santiagocasas/santiagocasas.github.io/actions/workflows/prettier.yml)

Personal academic website of Santiago Casas: theoretical physicist, cosmologist, and astrophysicist.

Live site: https://santiagocasas.github.io

This repository contains the source for my homepage, publications, projects, notes, slides, and CV.

The site is built with [Jekyll](https://jekyllrb.com/) and based on [al-folio](https://github.com/alshedivat/al-folio), a simple, clean, and responsive theme for academics.

## Local Preview

Clone the repository:

```bash
git clone https://github.com/santiagocasas/santiagocasas.github.io.git
cd santiagocasas.github.io
```

Make sure Docker is installed:

```bash
docker --version
docker compose version
```

If those commands fail, install Docker and Docker Compose first.

Start the site locally with Docker:

```bash
docker compose up
```

Then open `http://localhost:8080`.

To rebuild the site without starting the local server:

```bash
docker compose run --rm jekyll bash -lc "bundle install && bundle exec jekyll build"
```
