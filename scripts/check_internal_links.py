#!/usr/bin/env python3
"""Validate local href/src targets and HTML fragments in a built MkDocs site."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class PageScanner(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.references: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(attributes["id"])
        for name in ("href", "src"):
            if attributes.get(name):
                self.references.append(attributes[name])


def scan(path: Path) -> PageScanner:
    scanner = PageScanner()
    scanner.feed(path.read_text(encoding="utf-8"))
    return scanner


def main() -> int:
    if len(sys.argv) not in (2, 3):
        print("usage: check_internal_links.py SITE_DIR [BASE_PATH]", file=sys.stderr)
        return 2

    site = Path(sys.argv[1]).resolve()
    base_path = sys.argv[2] if len(sys.argv) == 3 else "/"
    if not base_path.startswith("/") or not base_path.endswith("/"):
        print("BASE_PATH must begin and end with '/'", file=sys.stderr)
        return 2
    if not site.is_dir():
        print(f"site directory does not exist: {site}", file=sys.stderr)
        return 2

    pages = sorted(site.rglob("*.html"))
    id_cache = {page: scan(page).ids for page in pages}
    failures: list[tuple[Path, str, str]] = []

    for page in pages:
        scanner = scan(page)
        for raw_reference in scanner.references:
            if raw_reference.startswith("//"):
                continue
            if raw_reference.startswith("#"):
                fragment = unquote(raw_reference[1:])
                if fragment and fragment not in scanner.ids:
                    failures.append((page, raw_reference, "missing same-page anchor"))
                continue

            url = urlsplit(raw_reference)
            if url.scheme in {"data", "http", "https", "javascript", "mailto", "tel"}:
                continue

            reference_path = unquote(url.path)
            if reference_path.startswith(base_path):
                target = site / reference_path[len(base_path) :]
            elif reference_path.startswith("/"):
                target = site / reference_path.lstrip("/")
            else:
                target = page.parent / reference_path
            if not reference_path:
                target = page

            target = target.resolve()
            try:
                target.relative_to(site)
            except ValueError:
                failures.append((page, raw_reference, "target escapes site directory"))
                continue

            candidate = target
            if candidate.is_dir() or reference_path.endswith("/"):
                candidate = candidate / "index.html"
            elif not candidate.exists() and not candidate.suffix:
                candidate = candidate / "index.html"

            if not candidate.exists():
                failures.append((page, raw_reference, "missing target"))
                continue

            if url.fragment and candidate.suffix == ".html":
                ids = id_cache.setdefault(candidate, scan(candidate).ids)
                if unquote(url.fragment) not in ids:
                    failures.append((page, raw_reference, "missing target anchor"))

    for page, reference, reason in failures:
        print(f"{page.relative_to(site)}: {reference}: {reason}")

    if failures:
        print(f"Internal link validation failed: {len(failures)} error(s)")
        return 1

    print(f"Internal link validation passed: {len(pages)} HTML page(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
