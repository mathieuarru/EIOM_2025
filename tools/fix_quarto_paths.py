#!/usr/bin/env python3
"""Fix Quarto path references.

- Build an index of files with extensions of interest.
- Scan project files and normalize references in YAML includes,
  knitr child directives, R file loaders and markdown links.

This script is idempotent and uses only the Python standard library.
"""
from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Dict, List

PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXTS = {".qmd", ".Rmd", ".md", ".R", ".html"}
PREF_ORDER = [".qmd", ".Rmd", ".md", ".R", ".html"]


def build_index() -> Dict[str, List[Path]]:
    index: Dict[str, List[Path]] = {}
    for path in PROJECT_ROOT.rglob('*'):
        if not path.is_file():
            continue
        if path.suffix not in EXTS:
            continue
        rel = path.relative_to(PROJECT_ROOT)
        parts = rel.parts
        if any(p in {".git", "_site", "_freeze", ".quarto"} or p.endswith("_files") for p in parts):
            continue
        index.setdefault(path.stem, []).append(rel)
    return index


def choose_candidate(stem: str, index: Dict[str, List[Path]]) -> Path | None:
    paths = index.get(stem)
    if not paths:
        return None
    paths = sorted(paths, key=lambda p: PREF_ORDER.index(p.suffix) if p.suffix in PREF_ORDER else 99)
    return PROJECT_ROOT / paths[0]


def normalize(path_str: str, base_dir: Path, index: Dict[str, List[Path]]) -> str:
    path = Path(path_str)
    if path.is_absolute():
        try:
            path = path.relative_to(PROJECT_ROOT)
        except ValueError:
            # outside project; leave as is
            return path_str
    candidate = (base_dir / path).resolve()
    if candidate.exists():
        return os.path.relpath(candidate, base_dir).replace(os.sep, "/")

    stem = path.stem
    if path.suffix == ".rmarkdown":
        for ext in (".qmd", ".Rmd", ".md"):
            alt = choose_candidate(stem, index)
            if alt and alt.suffix == ext:
                return os.path.relpath(alt, base_dir).replace(os.sep, "/")
    else:
        alt = choose_candidate(stem, index)
        if alt:
            return os.path.relpath(alt, base_dir).replace(os.sep, "/")
    return path_str


def process_file(path: Path, index: Dict[str, List[Path]]) -> int:
    text = path.read_text(encoding='utf-8')
    orig = text
    dirname = path.parent

    # YAML includes
    def repl_include(match: re.Match) -> str:
        prefix, quote, p = match.group(1), match.group(2), match.group(3)
        new_p = normalize(p, PROJECT_ROOT, index)
        return f"{prefix}{quote}{new_p}{quote}"

    text = re.sub(
        r'(?m)^(\s*include-(?:before-body|in-header|after-body):\s*)(["\'])([^"\']+)(["\'])',
        lambda m: repl_include(m),
        text,
    )
    # child chunks
    text = re.sub(r'(child\s*=\s*["\'])([^"\']+)(["\'])',
                  lambda m: f"{m.group(1)}{normalize(m.group(2), dirname, index)}{m.group(3)}", text)
    # R loaders
    text = re.sub(r'((?:source|readLines|read_file|readr::read_file)\(\s*["\'])([^"\']+)(["\']\s*\))',
                  lambda m: f"{m.group(1)}{normalize(m.group(2), dirname, index)}{m.group(3)}", text)
    # Markdown links
    text = re.sub(r'(\[[^\]]+\]\()([^\)]+)(\))',
                  lambda m: f"{m.group(1)}{normalize(m.group(2), dirname, index)}{m.group(3)}", text)

    if text != orig:
        path.write_text(text, encoding='utf-8')
        return 1
    return 0


def main() -> None:
    index = build_index()
    count = 0
    for path in PROJECT_ROOT.rglob('*'):
        if not path.is_file() or path.suffix not in EXTS:
            continue
        rel = path.relative_to(PROJECT_ROOT)
        parts = rel.parts
        if any(p in {".git", "_site", "_freeze", ".quarto"} or p.endswith("_files") for p in parts):
            continue
        count += process_file(path, index)
    print(f"Updated {count} file(s)")


if __name__ == "__main__":
    main()
