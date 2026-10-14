#!/usr/bin/env python3
"""Turn Dokka GFM output into Starlight-ready Markdown.

Usage: fix-dokka.py <content dir> <url base>
  e.g. fix-dokka.py src/content/docs/api/mods/potion_totems /docs/api/mods/potion_totems

What it does:
  * drops Dokka's breadcrumb lines (//[module](...)/...)
  * moves the first "# Title" into frontmatter (Starlight requires `title`)
  * turns package directories (io.github.x.y.block.entity) into a nested tree
    (block/entity), dropping the package prefix every package shares, so the
    sidebar is short and readable
  * labels every index page "Overview" in the sidebar
  * renames files/directories to URL-safe lowercase names
  * rewrites relative `.md` links to absolute Starlight URLs
  * flattens the module wrapper folder (-potion-totems/) away
  * turns Dokka's plain-text signatures into highlighted ```kotlin code blocks
    (Dokka writes Java declarations in Kotlin-style syntax)
  * removes the "[java]" source-set labels and Dokka's package-list file
  * tags other code fences with java/kotlin so Starlight highlights them
"""
import json
import html
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

root = Path(sys.argv[1])
base = sys.argv[2].rstrip("/")

# Signatures become fenced code blocks (syntax highlighted), but code blocks
# can't contain links, so type names stop being clickable. Set to False to keep
# Dokka's linked plain-text signatures instead.
HIGHLIGHT_SIGNATURES = True

LINK = re.compile(r'\]\((?!https?:|#|/|mailto:)([^)\s#]+?)\.md(#[^)\s]*)?\)')
FENCE_OPEN = re.compile(r'^(\s*)```([\w+-]*)\s*$')
FENCE_CLOSE = re.compile(r'^\s*```\s*$')
KOTLIN_KW = re.compile(r'\b(fun|val|var|object|typealias|suspend|inline|reified|companion|data class|sealed)\b')
JAVA_KW = re.compile(
    r'\b(public|protected|private|static|void|extends|implements|final|throws|new|'
    r'synchronized|package|import|abstract|@Override|System\.out)\b|;\s*$',
    re.M,
)


def slug(segment: str) -> str:
    s = re.sub(r"[^a-z0-9_-]+", "-", segment.lower())
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "x"


# ---- package directories -> nested directories -----------------------------
files = sorted(root.rglob("*.md"))
if not files:
    sys.exit(f"No .md files found in {root}")
rels = [f.relative_to(root) for f in files]

package_dirs = {d for rel in rels for d in rel.parts[:-1] if "." in d}
split_packages = [p.split(".") for p in package_dirs]
common = os.path.commonprefix(split_packages) if split_packages else []
strip = common[:-1]  # keep the last shared segment as the top node of the tree


def map_dirs(dirs):
    # Drop the module wrapper folder(s) that sit in front of the first package folder.
    first_pkg = next((i for i, d in enumerate(dirs) if "." in d), None)
    if first_pkg:
        dirs = dirs[first_pkg:]
    out = []
    for d in dirs:
        if "." in d:
            parts = d.split(".")
            if parts[: len(strip)] == strip:
                parts = parts[len(strip):]
            out.extend(slug(p) for p in parts)
        else:
            out.append(slug(d))
    return out


def new_rel(rel: Path) -> Path:
    *dirs, name = rel.parts
    stem = name[:-3]
    new_name = "index.md" if stem == "index" else f"{slug(stem)}.md"
    return Path(*map_dirs(dirs), new_name)


def rewrite_links(text: str, old_rel: Path) -> str:
    parent = old_rel.parent

    def repl(m: re.Match) -> str:
        target = os.path.normpath(os.path.join(str(parent), unquote(m.group(1))))
        if target.startswith(".."):
            return m.group(0)  # points outside this module, leave untouched
        *dirs, stem = [p for p in Path(target).parts if p != "."]
        segs = map_dirs(dirs) + ([] if stem == "index" else [slug(stem)])
        url = "/".join([base.lstrip("/")] + segs)
        return f"](/{url}/{m.group(2) or ''})"

    return LINK.sub(repl, text)


# ---- code fences ------------------------------------------------------------
def guess_lang(lang: str, code: str) -> str:
    if lang and lang != "text":
        return lang  # already tagged (incl. our signature blocks): keep as is
    is_kotlin = bool(KOTLIN_KW.search(code))
    is_java = bool(JAVA_KW.search(code))
    if is_kotlin and not is_java:
        return "kotlin"
    return "java"


def fix_fences(text: str) -> str:
    lines = text.split("\n")
    out, i = [], 0
    while i < len(lines):
        m = FENCE_OPEN.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        indent, lang = m.groups()
        j, block = i + 1, []
        while j < len(lines) and not FENCE_CLOSE.match(lines[j]):
            block.append(lines[j])
            j += 1
        out.append(f"{indent}```{guess_lang(lang, chr(10).join(block))}")
        out.extend(block)
        if j < len(lines):
            out.append(lines[j])
        i = j + 1
    return "\n".join(out)


# ---- signatures -------------------------------------------------------------
LINK_MD = re.compile(r'\[([^\]]*)\]\([^)]*\)')
SIG_MARK = re.compile(r'^\[\w+\]\\?$')       # "[java]\"
CELL_MARK = re.compile(r'\[\w+\]<br>')         # "[java]<br>" inside table cells


def plain(text: str) -> str:
    """Markdown with links/entities -> plain source text."""
    text = LINK_MD.sub(r"\1", text)
    text = html.unescape(text)
    return re.sub(r"\\([\\`*_{}\[\]()<>#+!.|-])", r"\1", text)


def convert_signatures(text: str) -> str:
    lines = text.split("\n")
    out, i = [], 0
    while i < len(lines):
        if not SIG_MARK.match(lines[i].strip()):
            out.append(CELL_MARK.sub("", lines[i]))
            i += 1
            continue
        j, sig = i + 1, []
        while j < len(lines):  # annotations first, then the declaration line
            cur = lines[j].strip()
            j += 1
            if not cur:
                continue
            sig.append(cur)
            if not cur.startswith("@"):
                break
        if HIGHLIGHT_SIGNATURES:
            out += ["```kotlin", *[plain(l) for l in sig], "```"]
        else:
            out += [*sig]
        i = j
    return "\n".join(out)


# ---- page conversion --------------------------------------------------------
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
    body = fix_fences(convert_signatures(body))
    front = f"title: {json.dumps(title)}\n"
    if rel.name == "index.md":
        front += 'sidebar:\n  label: "Overview"\n'
    return f"---\n{front}---\n\n{body}\n"


converted = {}
for f, rel in zip(files, rels):
    out = new_rel(rel)
    if out in converted:
        sys.exit(f"Name collision after slugifying: {rel} -> {out}")
    converted[out] = convert(f, rel)

for f in root.rglob("*"):
    if f.is_file():
        f.unlink()  # the .md files (re-written below) and Dokka's package-list
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