# -*- coding: utf-8 -*-
"""Every Promise — core translation utilities.

The app is a single 7.5 MB file (index.html) with four inline JS data blobs on
lines 378-381 (1-indexed): CHAPTERS, LEXICON, PROMISES, ABBOTT. Each blob is a
SINGLE LINE and must stay that way. These helpers load/edit/save the blobs while
preserving their exact single-line, UTF-8 (ensure_ascii=False) layout, so a small
edit yields a small, reviewable diff.

Never pretty-print the blobs. Never edit index.html by hand for data changes.
"""
import io, json, os, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(ROOT, "index.html")

PREFIXES = {
    "CHAPTERS": "const CHAPTERS = ",
    "LEXICON":  "const LEXICON = ",
    "PROMISES": "const PROMISES = ",
    "ABBOTT":   "const ABBOTT = ",
}

# 2026-07-20: the four blobs moved OUT of index.html into data/*.js, each still
# a single line with the same `const NAME = ...` prefix. index.html went 9.9 MB
# -> 50 KB, so a code edit no longer rewrites ten megabytes, and a promises
# update no longer touches the New Testament. Loaded by <script src> rather than
# fetch() specifically so the page still opens from file:// with no server.
FILES = {name: os.path.join(ROOT, "data", name.lower() + ".js") for name in PREFIXES}


class Workspace(object):
    """What read_lines() now returns.

    Every tool is written as:
        lines = ep.read_lines()
        _, CH = ep.load(lines, "CHAPTERS")
        ep.dump_into(lines, "CHAPTERS", CH)
        ep.write_lines(lines)
    Keeping that exact shape after the split means none of the ~20 tools needed
    editing. This object just remembers which blobs were loaded and which were
    changed, and writes back only the changed ones.
    """

    def __init__(self):
        self.obj = {}
        self.dirty = set()

# Documented invariants — verify after every session.
# 2026-07-17: 2 Corinthians (13 ch), Galatians (6), Ephesians (6), Philippians
# (4), Colossians (4), 1 Thessalonians (5), 2 Thessalonians (3), 1 Timothy (6),
# then 2 Timothy (4 ch, +1,048 units / +1,235 tokens) added, raising the
# baseline from the original 84,290 / 96,778.
# 2026-07-18: Titus (3 ch, +577 units / +659 tokens) added.
# 2026-07-18: Philemon (1 ch, +287 units / +334 tokens) added.
# 2026-07-18: Hebrews (13 ch, +4,113 units / +4,935 tokens) added.
# 2026-07-18: James (5 ch, +1,516 units / +1,739 tokens) added.
# 2026-07-18: 1 Peter (5 ch, +1,479 units / +1,678 tokens) added.
# 2026-07-18: 2 Peter (3 ch, +950 units / +1,098 tokens) added.
# 2026-07-18: 1 John (5 ch, +1,782 units / +2,137 tokens) added.
# 2026-07-18: 2 John (1 ch, +210 units / +245 tokens) added.
# 2026-07-18: 3 John (1 ch, +176 units / +219 tokens) added.
# 2026-07-18: Jude (1 ch, +404 units / +459 tokens) added.
# 2026-07-18: Revelation (22 ch, +7,853 units / +9,833 tokens) added.
# The entire New Testament is now present (Matthew through Revelation).
EXPECT_UNITS = 117353
EXPECT_TOKENS = 137554


def utf8_stdout():
    """Force UTF-8 stdout so Greek prints on Windows consoles (cp1252)."""
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def read_lines():
    """A handle on the data blobs. Keeps the name every tool already calls."""
    return Workspace()


def _find(lines, prefix):
    for i, ln in enumerate(lines):
        if ln.startswith(prefix):
            return i
    raise RuntimeError("prefix not found: " + prefix)


def _parse(line, name):
    body = line[len(PREFIXES[name]):].rstrip()
    if body.endswith(";"):
        body = body[:-1]
    return json.loads(body)


def load(source, name):
    """Return (0, parsed_object) for a named blob.

    `source` is normally the Workspace from read_lines(). It may ALSO be a plain
    list of lines -- that path is kept deliberately, because verification
    scripts compare against an older index.html pulled from git history, back
    when all four blobs still lived inside it.
    """
    if isinstance(source, Workspace):
        if name not in source.obj:
            with io.open(FILES[name], "r", encoding="utf-8", newline="") as f:
                source.obj[name] = _parse(f.readline(), name)
        return 0, source.obj[name]
    i = _find(source, PREFIXES[name])
    return i, _parse(source[i], name)


def dump_into(source, name, obj):
    """Stage obj to be written back to its blob."""
    if isinstance(source, Workspace):
        source.obj[name] = obj
        source.dirty.add(name)
        return source
    i = _find(source, PREFIXES[name])
    source[i] = PREFIXES[name] + json.dumps(obj, ensure_ascii=False) + ";"
    return source


def write_lines(source):
    """Write back only the blobs that changed -- one line each, layout intact."""
    if isinstance(source, Workspace):
        for name in sorted(source.dirty):
            with io.open(FILES[name], "w", encoding="utf-8", newline="\n") as f:
                f.write(PREFIXES[name] + json.dumps(source.obj[name], ensure_ascii=False) + ";\n")
        source.dirty.clear()
        return
    with io.open(HTML, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(source))


# ---- counting ----
def tokset(words):
    return Counter(t for w in words for t in w[1].split())


def section_tokens(words):
    return sum(len(w[1].split()) for w in words)


def total_tokens(chapters):
    return sum(len(w[1].split()) for c in chapters for s in c["sections"] for w in s["words"])


def total_units(chapters):
    return sum(1 for c in chapters for s in c["sections"] for w in s["words"])


def chapter_index(chapters, ref):
    """Index of a chapter by its ref string, e.g. 'Luke 7'."""
    for i, c in enumerate(chapters):
        if c["ref"] == ref:
            return i
    raise RuntimeError("chapter not found: " + ref)


# ---- the splice workhorse ----
def splice(ws, a, b, plan):
    """Replace ws[a:b] with units reordered per plan = [(old_abs_index, new_en|None), ...].

    new_en=None keeps the existing English. Asserts the plan covers exactly [a,b)
    once and that the Greek multiset of the span is unchanged (no Greek moved in
    or out). These assertions cannot catch gloss drift — that needs pair reading.
    """
    seg = [list(w) for w in ws[a:b]]
    assert sorted(i for i, _ in plan) == list(range(a, b)), \
        "plan must cover exactly [%d,%d)" % (a, b)
    new = []
    for i, en in plan:
        u = list(ws[i])
        if en is not None:
            u[0] = en
        new.append(u)
    assert Counter(t for w in seg for t in w[1].split()) == \
           Counter(t for w in new for t in w[1].split()), "splice changed Greek"
    ws[a:b] = new
