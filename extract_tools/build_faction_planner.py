#!/usr/bin/env python3
"""build_faction_planner.py -- rebuild artifacts/faction_planner.html from the guide's corpus.

    python extract_tools/build_faction_planner.py            # writes artifacts/faction_planner.html
    python extract_tools/build_faction_planner.py --report   # also prints per-faction counts

How it works
------------
1. corpus_blocks.py parses every corpus markdown file into claim blocks (the paragraph or
   table above a `_source:` line) with their tier tags. Tables are split into row facts.
2. RULES below say which blocks go into which planner section, for which faction. A rule
   matches on file, heading, an optional first-line pattern and (for entity rules) the
   block's own `entity:` tag. A rule that matches nothing is an error: the corpus moved.
3. The facts are written, with their file:line pointer and the tags the corpus gave them,
   into extract_tools/faction_planner_template.html at the DATA marker.

Nothing here is invented: every fact line is corpus text; the only thing added is which
section it sits in. Facts that are not picked by a rule are simply not shown.
Standard library only.
"""

import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import corpus_blocks as cb  # noqa: E402

SECTIONS = [
    ("playstyle", "Playstyle and unique mechanics"),
    ("people", "Heroes, councillors and operations"),
    ("traits", "Conquest starting traits"),
    ("opening", "Opening and build order"),
    ("landsraad", "Landsraad and Governorship"),
    ("wins", "Win conditions it leans toward"),
]

SPOIL_RANK = {"none": 0, "progression": 1, "late-game": 2, "story": 3}

# ---- rules --------------------------------------------------------------------------------
# scope "own":    block carries entity: <this faction>
# scope "shared": no entity needed; shown for every faction (once, in the "same for all" part)
# file may contain {id}. h2/start are regexes (re.search); kw filters paragraph text.
# rows: None = split every table row; "faction" = keep only this faction's row (first cell
# starts with the faction id); a string = regex the row's first cell must match.
RULES = [
    # playstyle and unique mechanics
    dict(section="playstyle", scope="own", file="factions/{id}.md",
         h2=r"^(Bonuses|Strengths, weaknesses, counters|Overview and bonuses|The Nodal Network and Neural Nodes|Tethering|Fuel Cells|Patents, obfuscation and Analytical Machines|Unique developments and buildings)$"),
    dict(section="playstyle", scope="own", file="items/upgrades.md"),
    dict(section="playstyle", scope="own", file="items/developments.md"),
    # heroes, councillors, operations
    # Vernius's councillor table in abilities.md repeats the richer one in its own file: skip the repeat
    dict(section="people", scope="own", file="items/abilities.md", skip_for={"vernius": r"^\| Councilor "}),
    dict(section="people", scope="own", file="factions/{id}.md", h2=r"^Councilors$"),
    dict(section="people", scope="own", file="factions/{id}.md", start=r"^\| Hero "),
    dict(section="people", scope="shared", file="mechanics.md", h2=r"^Heroes$"),
    dict(section="people", scope="shared", file="sections/conflicts.md", h2=r"^Open conflicts$",
         start=r"^\| Topic ", rows=r"^First hero pick cost"),
    # Conquest starting traits and house features
    dict(section="traits", scope="shared", file="sections/conquest.md", h2=r"^Starting traits per house$",
         start=r"^\| House ", rows="faction"),
    dict(section="traits", scope="own", file="sections/conquest.md"),
    dict(section="traits", scope="own", file="factions/{id}.md", h2=r"^(Conquest|Vernius in Conquest)$"),
    # opening and build order
    dict(section="opening", scope="own", file="items/builds.md"),
    dict(section="opening", scope="own", file="factions/{id}.md", h2=r"^Playing Vernius in skirmish and multiplayer$"),
    dict(section="opening", scope="shared", file="items/builds.md", h2=r"^Generic opening \(all factions\)$"),
    # Landsraad and Governorship
    dict(section="landsraad", scope="own", file="sections/landsraad.md"),
    dict(section="landsraad", scope="own", file="factions/{id}.md",
         kw=r"Landsraad|Standing|Charter|Governor|Resolution", h2=r"^(Bonuses|Strengths, weaknesses, counters|Overview and bonuses|The Nodal Network and Neural Nodes|Patents, obfuscation and Analytical Machines|Councilors|Unique developments and buildings)$",
         paragraphs_only=True),
    dict(section="landsraad", scope="shared", file="sections/landsraad.md", h2=r"^Landsraad Standing: gains and losses$", start=r"^Standing runs"),
    dict(section="landsraad", scope="shared", file="sections/landsraad.md", h2=r"^Dune Governorship"),
    dict(section="landsraad", scope="shared", file="mechanics.md", h2=r"^Landsraad, council and CHOAM$",
         start=r"^\| Charter ", rows=r"^Dune Governorship"),
    dict(section="landsraad", scope="shared", file="mechanics.md", h2=r"^Landsraad, council and CHOAM$",
         start=r"^An Atreides at 10,000 Hegemony needs only the Standing"),
    # win conditions
    dict(section="wins", scope="shared", file="mechanics.md", h2=r"^Victory conditions$"),
    dict(section="wins", scope="shared", file="items/builds.md", h2=r"^AI behaviour that shapes openings$"),
    dict(section="wins", scope="own", file="items/builds.md",
         kw=r"(?i)governorship|CHOAM|victory|win by|wins by|won by|political|economic|hegemony|assassinat"),
    dict(section="wins", scope="own", file="factions/{id}.md", h2=r"^Strengths, weaknesses, counters$",
         kw=r"(?i)governorship|CHOAM|victory|political|economic play|hegemony"),
]

FACTION_ORDER = ["atreides", "harkonnen", "smugglers", "fremen", "corrino", "ecaz", "vernius"]


def clean(t):
    t = t.replace("`", "")
    t = t.replace("**", "")
    return t.strip()


def tier_of(b):
    """(enemy tier, decision tier, spoiler tag) of a block, as its own _source line gives them."""
    t = b["tags"]
    return int(t.get("enemy-tier", "0") or 0), int(t.get("puzzle-tier", "0") or 0), t.get("spoiler", "none")


def label_kind(label):
    """Return (kind, text) from the corroboration label(s) after the _source line."""
    if not label:
        return "none", ""
    first = re.findall(r"\[([^\]]*)\]", label)
    kind, extra = "none", []
    for item in first:
        if item.startswith("Single source"):
            kind = "single"
        elif item.startswith("Confirmed"):
            m = re.match(r"Confirmed:\s*(\d+)", item)
            kind = "confirmed:" + (m.group(1) if m else "2")
        elif item.startswith("Contradicted"):
            kind = "contradicted"
        elif item.startswith("Hypothesis"):
            kind = "hypothesis"
        else:
            extra.append(item)
    return kind, "; ".join(extra)


def facts_from_block(b, rule, fid_prefix, faction_names):
    """Turn one block into one or more fact dicts (tables become row facts)."""
    tags = b["tags"]
    kind, extra = label_kind(b["label"])
    base = {
        "f": b["file"],
        "e": int(tags.get("enemy-tier", "0") or 0),
        "p": int(tags.get("puzzle-tier", "0") or 0),
        "s": tags.get("spoiler", "none"),
        "c": tags.get("confidence", ""),
        "lab": kind,
        "x": extra,
        "d": b["date"],
        "n": len(b["urls"]),
    }
    out = []
    tbl = cb.table_rows(b)
    if tbl:
        header, rows = tbl
        tier_col = header.index("tier") if "tier" in header else None
        for lineno, cells in rows:
            if not cells or not cells[0]:
                continue
            rowmatch = rule.get("rows")
            first = cells[0].lower()
            if rowmatch == "faction":
                if not first.startswith(fid_prefix):
                    continue
            elif isinstance(rowmatch, str):
                if not re.search(rowmatch, cells[0]):
                    continue
            f = dict(base)
            f["l"] = lineno
            f["title"] = clean(cells[0])
            if header[0] in ("friendship", "unity"):
                f["title"] = header[0].capitalize() + " " + f["title"]
            parts = []
            if header[0] == "category" and len(cells) > 1:
                # category tables name the item in column 2: title it by that, keep the category as a part
                f["title"] = clean(cells[1])
                parts.append(("Category", clean(cells[0])))
                skip_cols = {1}
            else:
                skip_cols = set()
            for k, v in enumerate(cells[1:], start=1):
                if k in skip_cols:
                    continue
                if tier_col is not None and k == tier_col:
                    continue
                if k < len(header) and v:
                    parts.append((clean(header[k]).capitalize(), clean(v)))
            f["rowparts"] = parts
            f["t"] = ""
            if tier_col is not None and tier_col < len(cells) and cells[tier_col]:
                f["s"] = cells[tier_col].strip()
            out.append(f)
        return out
    text = clean(" ".join(b["lines"]))
    f = dict(base)
    f["l"] = b["line"]
    f["t"] = text
    out.append(f)
    return out


def main():
    report = "--report" in sys.argv
    files = [p for p in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)
             if not any(x in p.replace("\\", "/") for x in ("/_overflow/", "/extract_tools/", "/artifacts/"))]
    blocks = []
    for p in sorted(files):
        rel = os.path.relpath(p, ROOT).replace("\\", "/")
        blocks.extend(cb.parse_file(p, rel))

    # faction roster from factions/index.md
    roster = {}
    roster_line = {}
    for b in blocks:
        if b["file"] == "factions/index.md" and cb.table_rows(b) and b["lines"][0].startswith("| entity-id"):
            for rline, cells in cb.table_rows(b)[1]:
                roster[cells[0]] = cells[1]
                roster_line[cells[0]] = rline
    assert set(roster) == set(FACTION_ORDER), "faction roster changed: " + str(sorted(roster))

    # leaders from the abilities summary table, Vernius from its own overview line
    leaders = {}
    glance = {}
    for b in blocks:
        if b["file"] == "items/abilities.md" and b["lines"][0].startswith("| Faction | Leader"):
            for _, cells in cb.table_rows(b)[1]:
                leaders[cells[0].lower()] = (clean(cells[1]), b["line"])
                ge, gp, gs = tier_of(b)
                glance[cells[0].lower()] = {
                    "councillors": [x.strip() for x in clean(cells[2]).split(",")],
                    "heroes": [x.strip() for x in clean(cells[3]).split(",")],
                    "ptr": "items/abilities.md:%d" % b["line"],
                    # the source table's own tier tags: the card names are gated by them like any fact
                    "e": ge, "p": gp, "s": gs,
                }
    # Vernius is not in that summary table: take the names from its own councillor and hero rows
    vc, vh = [], []
    vtags = []
    for b in blocks:
        t = cb.table_rows(b)
        if not t:
            continue
        if b["file"] == "items/abilities.md" and b["h2"].startswith("House Vernius") and b["lines"][0].startswith("| Councilor"):
            vc = [clean(c[0]) for _, c in t[1]]
            vptr = "items/abilities.md:%d" % b["line"]
            vtags.append(tier_of(b))
        if b["file"] == "factions/vernius.md" and b["lines"][0].startswith("| Hero "):
            vh = [clean(c[0]) for _, c in t[1]]
            vtags.append(tier_of(b))
    assert vc and vh, "Vernius councillor or hero names not found"
    # both sources must pass for the names to show: take the stricter enemy and decision tier
    glance["vernius"] = {"councillors": vc, "heroes": vh, "ptr": vptr,
                         "e": max(x[0] for x in vtags), "p": max(x[1] for x in vtags), "s": vtags[0][2]}
    m = None
    for b in blocks:
        if b["file"] == "factions/vernius.md":
            m = re.search(r"Leader:\s*([^.]+)\.", " ".join(b["lines"]))
            if m:
                leaders["vernius"] = (m.group(1).strip(), b["line"])
                break
    for fid in FACTION_ORDER:
        assert fid in leaders, "no leader found for " + fid

    short = {fid: fid.capitalize() for fid in FACTION_ORDER}
    mention = {fid: re.compile(r"\b" + short[fid] + r"\w*", re.I) for fid in FACTION_ORDER}

    facts = {}             # id -> fact
    plan = {fid: {s: {"own": [], "shared": []} for s, _ in SECTIONS} for fid in FACTION_ORDER}
    shared_registry = {}   # (section, fid-less) for dedupe of shared facts
    rule_hits = [0] * len(RULES)

    def register(fact, faction, rule, ri):
        fid_key = "%s:%d" % (fact["f"], fact["l"])
        if fid_key not in facts:
            facts[fid_key] = fact
        sec = rule["section"]
        slot = plan[faction][sec]["own" if rule["scope"] == "own" else "shared"]
        if fid_key not in slot:
            slot.append(fid_key)
        rule_hits[ri] += 1

    for ri, rule in enumerate(RULES):
        for b in blocks:
            if rule.get("start") and not re.search(rule["start"], b["lines"][0]):
                continue
            if rule.get("h2") and not re.search(rule["h2"], b["h2"]):
                continue
            if rule.get("kw") and not re.search(rule["kw"], " ".join(b["lines"])):
                continue
            if rule.get("paragraphs_only") and cb.table_rows(b):
                continue
            if rule["scope"] == "own":
                ent = b["tags"].get("entity")
                if not ent or ent not in FACTION_ORDER:
                    continue
                skip = rule.get("skip_for", {}).get(ent)
                if skip and re.search(skip, b["lines"][0]):
                    continue
                if "{id}" in rule["file"]:
                    if b["file"] != rule["file"].replace("{id}", ent):
                        continue
                elif b["file"] != rule["file"]:
                    continue
                for f in facts_from_block(b, rule, ent, short):
                    register(f, ent, rule, ri)
            else:
                if b["file"] != rule["file"]:
                    continue
                for fid in FACTION_ORDER:
                    for f in facts_from_block(b, rule, fid, short):
                        register(f, fid, rule, ri)
        if rule_hits[ri] == 0:
            raise SystemExit("rule %d matched nothing (corpus moved?): %r" % (ri, rule))

    # a shared "faction row" rule (starting traits) yields a per-faction row: keep it as that faction's own fact
    for fid in FACTION_ORDER:
        for sec, _ in SECTIONS:
            slot = plan[fid][sec]
            keep = []
            for k in slot["shared"]:
                if facts[k].get("title", "").lower().startswith(fid) and sec == "traits":
                    slot["own"].append(k)
                else:
                    keep.append(k)
            slot["shared"] = keep

    # order by (file order of first rule hit is not tracked) -> corpus order inside each list
    def sortkey(k):
        f = facts[k]
        return (f["f"], f["l"])

    for fid in FACTION_ORDER:
        for sec, _ in SECTIONS:
            for part in ("own", "shared"):
                plan[fid][sec][part].sort(key=sortkey)

    # the guide's dials
    wt = open(os.path.join(ROOT, "warning_tiers.md"), encoding="utf-8").read()
    me = re.search(r"\*\*Enemies:\s*Tier\s*(\d)\*\*", wt)
    mp = re.search(r"\*\*Puzzles:\s*Tier\s*(\d)\*\*", wt)
    assert me and mp, "warning_tiers.md dials not found"
    # optional third setting: "- **Paid DLC: Off** -- set <date>"; absent means the page starts with the DLC shown
    md = re.search(r"\*\*Paid DLC:\s*(On|Off)\*\*", wt)
    dlc_default = (md.group(1) == "On") if md else True

    # mark which shared facts name each faction (for highlighting)
    names_in = {}
    for k, f in facts.items():
        txt = f.get("t", "") + " " + f.get("title", "") + " " + " ".join(v for _, v in f.get("rowparts", []))
        names_in[k] = [fid for fid in FACTION_ORDER if mention[fid].search(txt)]

    factions = []
    for fid in FACTION_ORDER:
        disp = roster[fid]
        dlc = None
        if "(paid DLC)" in disp:
            disp = disp.replace("(paid DLC)", "").strip()
            dlc = disp.replace("House ", "")
        lead, lline = leaders[fid]
        factions.append({
            "id": fid, "name": disp, "leader": lead, "leaderPtr": ("items/abilities.md:%d" % lline) if fid != "vernius" else ("factions/vernius.md:%d" % lline),
            "dlc": dlc,
            "rosterPtr": "factions/index.md:%d" % roster_line[fid],
            "glance": glance[fid],
            "sections": plan[fid],
        })

    used = sorted({k for fid in FACTION_ORDER for s, _ in SECTIONS for part in ("own", "shared") for k in plan[fid][s][part]})
    data = {
        "guide": "Dune: Spice Wars",
        "dials": {"enemy": int(me.group(1)), "puzzle": int(mp.group(1)), "enemyMax": 5, "puzzleMax": 3, "dlc": dlc_default, "ptr": "warning_tiers.md:7-8"},
        "sections": [{"id": s, "name": n} for s, n in SECTIONS],
        "factions": factions,
        "facts": {k: facts[k] for k in used},
        "names": {k: names_in[k] for k in used},
        "spoilRank": SPOIL_RANK,
    }
    with open(os.path.join(HERE, "faction_planner_template.html"), encoding="utf-8") as fh:
        tpl = fh.read()
    assert "/*__DATA__*/" in tpl
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = tpl.replace("/*__DATA__*/null", blob)
    out_dir = os.path.join(ROOT, "artifacts")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "faction_planner.html")
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(html)

    # tallies
    def vis(f, e=data["dials"]["enemy"], p=data["dials"]["puzzle"], sp=1):
        # a dlc: fact ranks by its own enemy/decision depth (claim_format.md: tier-of-dlc-content), as the page does
        rank = SPOIL_RANK.get(f["s"], min(3, max(f["e"], f["p"])) if f["s"].startswith("dlc") else 3)
        return f["e"] <= e and f["p"] <= p and rank <= sp

    hidden_default = [k for k in used if not vis(facts[k])]
    print("wrote", out, "(%d bytes)" % len(html.encode("utf-8")))
    print("factions %d, distinct facts %d, hidden at default dials (enemy %d, puzzle %d, spoiler reach progression) %d"
          % (len(factions), len(used), data["dials"]["enemy"], data["dials"]["puzzle"], len(hidden_default)))
    if report:
        for fid in FACTION_ORDER:
            row = []
            for sec, _ in SECTIONS:
                o = plan[fid][sec]["own"]
                s = plan[fid][sec]["shared"]
                row.append("%s %d+%d" % (sec, len(o), len(s)))
            ownall = {k for sec, _ in SECTIONS for k in plan[fid][sec]["own"]}
            print("  %-10s %s | own facts %d, hidden at default %d" % (fid, "; ".join(row), len(ownall), sum(1 for k in ownall if not vis(facts[k]))))
        print("  rule hits:", rule_hits)


if __name__ == "__main__":
    main()
