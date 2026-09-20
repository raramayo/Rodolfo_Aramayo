# Aramayo Lab · Rodolfo Aramayo — research website

This repository contains the public source for the Aramayo Lab and Rodolfo Aramayo research website, built with MkDocs Material and published through GitHub Pages. It presents the laboratory's research program, current and former researcher contributions, teaching, publications, software, and collaboration profile.

## Local preview

The site is pinned to CPython 3.14.6. Confirm that `python3.14 --version`
reports `Python 3.14.6`, then create an isolated environment:

If that command selects a different patch version, use the full path to your
3.14.6 interpreter instead. Do not change the runtime pin just to match a
different Python earlier on your shell's search path.

```bash
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m mkdocs serve
```

Open `http://127.0.0.1:8000/Rodolfo_Aramayo/` in a browser.

## Validation

```bash
python -m pip check
python -m mkdocs build --clean --strict
python -B scripts/check_internal_links.py site /Rodolfo_Aramayo/
cmp -s docs/07_Resume_Rodolfo_Aramayo.pdf \
  docs/assets/documents/Rodolfo-Aramayo-Biotech-AI-Resume.pdf
```

The deployment workflow validates the site before publishing changes from the `main` branch.

## What belongs in the public repository

Commit the site sources: `docs/` (including **all curated `docs/assets/` files**),
`overrides/`, `scripts/check_internal_links.py`, `mkdocs.yml`, `requirements.txt`,
this README, `.gitignore`, and `.github/workflows/ci.yml`.

Do **not** commit `site/`, `.venv/`, caches, private source documents, or
development notes. `mkdocs serve` and `mkdocs build` generate `site/` locally;
the deployment workflow builds and publishes its own output. The portrait,
social-sharing image, and two-page PDF under `docs/assets/` are intentional
public assets, not private working files.

If this checkout has moved, recreate its virtual environment: installed command
launchers and activation scripts contain absolute paths. Prefer the
`python -m mkdocs` commands above to make the selected interpreter explicit.

## GitHub Pages setup

The workflow publishes the generated site to the `gh-pages` branch. In the
repository's **Settings → Pages**, select **Deploy from a branch**, then choose
`gh-pages` and `/ (root)`. The repository's Actions policy must allow the
workflow token to write repository contents.

## Updating the public résumé

Editable résumé sources and build artifacts are maintained separately from this public repository. They must not be committed or published. The stable visitor-facing résumé is:

- `docs/assets/documents/Rodolfo-Aramayo-Biotech-AI-Resume.pdf`

When the résumé changes, replace both public copies, update the visible date and page count in `docs/07_cv_contact.md`, and run the strict build before deployment. The legacy `docs/07_Resume_Rodolfo_Aramayo.pdf` path is retained for existing inbound links and must remain byte-identical to the stable two-page résumé.
