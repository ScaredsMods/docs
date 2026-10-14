#!/usr/bin/env python3
"""Turn Dokka GFM output into Starlight-ready Markdown.

Usage: fix-dokka.py <content dir> <url base>
  e.g. fix-dokka.py src/content/docs/api/mods/potion_totems /api/mods/potion_totems

What it does:
  * drops Dokka's breadcrumb lines (//[module](...)/...)
  * moves the first "# Title" into frontmatter (Starlight requires `title`)
  * renames files/directories to URL-safe lowercase names (Starlight slugifies
    paths, which would otherwise break dots, capitals, etc.)
  * rewrites relative `.md` links to absolute Starlight URLs
"""
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

root = Path(sys.argv[1])
base = sys.argv[2].rstrip("/")

LINK = re.compile(r'\]\((?!https?:|#|/|mailto:)([^)\s#]+?)\.md(#[^)\s]*)?\)')


def slug(segment: str) -> str:
    s = re.sub(r"[^a-z0-9_-]+", "-", segment.lower()).strip("-")
    return s or "x"


def new_rel(rel: Path) -> Path:
    *dirs, name = rel.parts
    stem = name[:-3]  # strip .md
    new_name = "index.md" if stem == "index" else f"{slug(stem)}.md"
    return Path(*[slug(d) for d in dirs], new_name)


def rewrite_links(text: str, old_rel: Path) -> str:
    parent = old_rel.parent

    def repl(m: re.Match) -> str:
        target = os.path.normpath(os.path.join(str(parent), unquote(m.group(1))))
        if target.startswith(".."):
            return m.group(0)  # points outside this module, leave untouched
        segs = [slug(s) for s in Path(target).parts if s != "."]
        if segs and segs[-1] == "index":
            segs.pop()
        url = "/".join([base.lstrip("/")] + segs)
        return f"](/{url}/{m.group(2) or ''})"

    return LINK.sub(repl, text)


def convert(path: Path, rel: Path) -> str:
    lines = [l for l in path.read_text(encoding="utf-8").splitlines()
             if not l.startswith("//[")]
    title = rel.parent.name or root.name
    for i, l in enumerate(lines):
        if l.startswith("# "):
            title = re.sub(r"\\(.)", r"\1", l[2:].strip())  # unescape \< \> \_
            del lines[i]  # Starlight renders the title as the page H1
            break
    body = rewrite_links("\n".join(lines).strip(), rel)
    return f"---\ntitle: {json.dumps(title)}\n---\n\n{body}\n"


files = sorted(root.rglob("*.md"))
if not files:
    sys.exit(f"No .md files found in {root}")

converted = {}
for f in files:
    rel = f.relative_to(root)
    out = new_rel(rel)
    if out in converted:
        sys.exit(f"Name collision after slugifying: {rel} -> {out}")
    converted[out] = convert(f, rel)

for f in files:
    f.unlink()
for d in sorted((p for p in root.rglob("*") if p.is_dir()), reverse=True):
    try:
        d.rmdir()
    except OSError:
        pass

for rel, text in converted.items():
    target = root / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")

print(f"Converted {len(converted)} pages in {root}")