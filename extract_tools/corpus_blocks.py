#!/usr/bin/env python3
"""corpus_blocks.py -- parse a Hintforge guide's markdown into claim blocks.

A claim block is the paragraph, table or list that sits directly above a `_source:` line
(the reach rule in builder/templates/claim_format.md). Each block keeps its file, line
numbers, heading path and the tags its `_source:` line carries. Tables are also split into
row facts, each row inheriting the block's tags, with the row's own `tier` column
overriding the spoiler tag (a row overrides the table tag, per claim_format.md).

Used by build_faction_planner.py. Standard library only.
"""

import re

SRC_RE = re.compile(
    r"^_source:\s*(?P<urls>.*?)\s+(?P<date>\d{4}-\d{2}-\d{2})\s+·\s+(?P<tags>.*?)_\s*(?P<label>(?:\[.*\]\s*)*)$"
)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")


def parse_tags(raw):
    tags = {}
    for part in raw.split(" · "):
        if ":" in part:
            k, v = part.split(":", 1)
            tags[k.strip()] = v.strip()
    return tags


def split_row(line):
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return cells


def is_sep(line):
    return bool(re.match(r"^\|?\s*:?-{2,}", line.strip().strip("|").strip())) and "|" in line


def parse_file(path, rel):
    """Return a list of block dicts for one markdown file."""
    with open(path, "r", encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    blocks = []
    heads = {}          # level -> text
    para = []           # (lineno, text)
    prev_blank = True
    i = 0
    n = len(lines)
    last_block_end = -1
    while i < n:
        line = lines[i]
        s = line.strip()
        m = HEADING_RE.match(line)
        if m and not line.startswith(" "):
            lvl = len(m.group(1))
            heads[lvl] = m.group(2)
            for k in list(heads):
                if k > lvl:
                    del heads[k]
            para = []
            i += 1
            continue
        if s.startswith("_source:"):
            sm = SRC_RE.match(s)
            if sm and para:
                tags = parse_tags(sm.group("tags"))
                urls = [u.strip() for u in sm.group("urls").split(" , ") if u.strip()]
                label = sm.group("label").strip()
                text_lines = [t for _, t in para]
                start = para[0][0]
                blocks.append({
                    "file": rel,
                    "line": start,
                    "end": i + 1,
                    "src_line": i + 1,
                    "h2": heads.get(2, ""),
                    "h3": heads.get(3, ""),
                    "h1": heads.get(1, ""),
                    "lines": text_lines,
                    "urls": urls,
                    "date": sm.group("date"),
                    "tags": tags,
                    "label": label,
                })
            para = []
            i += 1
            continue
        if s == "":
            # a blank line ends a paragraph unless the next non-blank line is its _source line
            j = i + 1
            while j < n and lines[j].strip() == "":
                j += 1
            if not (j < n and lines[j].strip().startswith("_source:")):
                para = []
            i += 1
            continue
        if s.startswith(">"):
            para = []
            i += 1
            continue
        para.append((i + 1, s))
        i += 1
    return blocks


def block_text(b):
    return "\n".join(b["lines"])


def table_rows(b):
    """If the block is a table, return (header, rows) else None. Each row: list of cells."""
    ls = b["lines"]
    if len(ls) >= 3 and ls[0].startswith("|") and is_sep(ls[1]):
        header = [h.lower() for h in split_row(ls[0])]
        rows = []
        for k, l in enumerate(ls[2:]):
            if l.startswith("|"):
                rows.append((b["line"] + 2 + k, split_row(l)))
        return header, rows
    return None
