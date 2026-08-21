# Aramayo Lab · Rodolfo Aramayo — research website

This repository contains the public source for the Aramayo Lab and Rodolfo Aramayo research website, built with MkDocs Material and published through GitHub Pages. It presents the laboratory's research program, current and former researcher contributions, teaching, publications, software, and collaboration profile.

## Local preview

The site is pinned to CPython 3.14.6. Confirm that `python3.14 --version`
reports `Python 3.14.6`, then create an isolated environment:

```bash
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs serve
```

Open `http://127.0.0.1:8000/Rodolfo_Aramayo/` in a browser.

## Validation

```bash
python -m pip check
mkdocs build --clean --strict
python -B scripts/check_internal_links.py site /Rodolfo_Aramayo/
cmp -s docs/07_Resume_Rodolfo_Aramayo.pdf \
  docs/assets/documents/Rodolfo-Aramayo-Biotech-AI-Resume.pdf
```

The deployment workflow validates the site before publishing changes from the `main` branch.

## GitHub Pages setup

The workflow publishes the generated site to the `gh-pages` branch. In the
repository's **Settings → Pages**, select **Deploy from a branch**, then choose
`gh-pages` and `/ (root)`. The repository's Actions policy must allow the
workflow token to write repository contents.

## Updating the public résumé

Editable résumé sources and build artifacts are maintained separately from this public repository. They must not be committed or published. The stable visitor-facing résumé is:

- `docs/assets/documents/Rodolfo-Aramayo-Biotech-AI-Resume.pdf`

When the résumé changes, replace both public copies, update the visible date and page count in `docs/07_cv_contact.md`, and run the strict build before deployment. The legacy `docs/07_Resume_Rodolfo_Aramayo.pdf` path is retained for existing inbound links and must remain byte-identical to the stable two-page résumé.
