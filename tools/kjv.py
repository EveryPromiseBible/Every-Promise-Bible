# -*- coding: utf-8 -*-
"""KJV lookup, so promise verses are QUOTED from a source rather than recalled.

The 329 existing promises are KJV. Adding hundreds more means producing hundreds
of verse texts, and generating scripture from memory is the one failure this
project cannot absorb: a misquoted verse is worse than any gloss defect we spent
the audit fixing, because it is the actual content, and nothing downstream would
flag it. So every new verse is looked up here and copied verbatim.

Source: scrollmapper/bible_databases, KJV (1769). Public domain.

Reference parsing handles the forms actually used in PROMISES -- "Psalm 46:1",
"1 John 4:8", "Song of Solomon 2:4" -- plus the singular/plural book-name
variants that differ between our data and the source (Psalm/Psalms,
Revelation/Revelation of John).

  python tools/kjv.py "Romans 8:28"       # print one verse
  python tools/kjv.py --verify            # check every existing promise matches
"""
import json, os, re, sys, io

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "KJV.json")

# Our reference spelling -> source spelling. The source numbers books with roman
# numerals ("i corinthians") and names the apocalypse "revelation of john", so
# every numbered book needs a mapping or it silently reports NOT FOUND.
ALIAS = {
    "psalm": "psalms", "song of songs": "song of solomon", "canticles": "song of solomon",
    "revelation": "revelation of john",
}
for _n, _r in ((1, "i"), (2, "ii"), (3, "iii")):
    for _b in ("samuel", "kings", "chronicles", "corinthians", "thessalonians",
               "timothy", "peter", "john"):
        ALIAS["%d %s" % (_n, _b)] = "%s %s" % (_r, _b)

_INDEX = None


def _norm(s):
    """Lowercase, collapse whitespace, and fold typography.

    Our data and the source disagree on apostrophes ("name's" vs "name’s") and
    on bracketing punctuation. Those are not quotation differences and must not
    be reported as ones, or the real signal drowns.
    """
    s = (s or "").strip().lower()
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("—", " ").replace("–", "-")
    s = re.sub(r"[()\[\]]", "", s)
    return re.sub(r"\s+", " ", s)


def index():
    """{(book, chapter, verse): text}, book normalised lowercase."""
    global _INDEX
    if _INDEX is None:
        with io.open(DATA, encoding="utf-8") as fh:
            d = json.load(fh)
        _INDEX = {}
        for b in d["books"]:
            bn = _norm(b["name"])
            for ch in b["chapters"]:
                for v in ch["verses"]:
                    _INDEX[(bn, int(ch["chapter"]), int(v["verse"]))] = v["text"].strip()
    return _INDEX


def parse(ref):
    """'1 John 4:8' -> ('i john', 4, 8, 8); '2 Cor 5:17-18' -> (..., 17, 18)."""
    m = re.match(r"^\s*(.+?)\s+(\d+):(\d+)(?:\s*[-–]\s*(\d+))?\s*$", ref or "")
    if not m:
        return None
    book = _norm(m.group(1))
    book = ALIAS.get(book, book)
    a = int(m.group(3))
    b = int(m.group(4)) if m.group(4) else a
    return book, int(m.group(2)), a, b


def lookup(ref):
    """Verbatim KJV text for a reference, joining a verse range with a space."""
    key = parse(ref)
    if not key:
        return None
    book, ch, a, b = key
    idx = index()
    parts = []
    for v in range(a, b + 1):
        t = idx.get((book, ch, v))
        if t is None:
            return None
        parts.append(t)
    return " ".join(parts)


def books():
    return sorted({k[0] for k in index()})


def faithful(ours, src):
    """Is `ours` an honest quotation of `src`?

    Not equality. The existing promises deliberately EXCERPT: Titus 3:5 stops at
    "he saved us." though the verse runs on, and some elide the middle with an
    ellipsis. Both are legitimate editorial choices, so the test is containment,
    not identity -- every fragment of our text must appear verbatim in the
    source, in order. That still catches the thing that matters: a word we
    invented, or a verse we misremembered.
    """
    if not ours or not src:
        return False
    s = _norm(src)
    pos = 0
    for frag in re.split(r"\s*\.\.\.\s*|\s*…\s*", _norm(ours)):
        frag = frag.strip(" .,;:")
        if not frag:
            continue
        at = s.find(frag, pos)
        if at < 0:
            return False
        pos = at + len(frag)
    return True


def verify_existing():
    """Calibration: if our 329 known-good verses check out, the lookup is
    trustworthy for the ones we add."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import epcore as ep
    _, P = ep.load(ep.read_lines(), "PROMISES")
    ok = miss = diff = 0
    problems = []
    for p in P:
        src = lookup(p["reference"])
        if src is None:
            miss += 1
            problems.append(("NOT FOUND", p["reference"], p["verse"][:70], ""))
        elif faithful(p["verse"], src):
            ok += 1
        else:
            diff += 1
            problems.append(("DIFFERS", p["reference"], p["verse"][:70], src[:70]))
    return ok, miss, diff, problems


def main():
    import epcore as ep
    ep.utf8_stdout()
    if "--verify" in sys.argv:
        ok, miss, diff, problems = verify_existing()
        for kind, ref, ours, theirs in problems[:40]:
            print("  %-9s %-22s" % (kind, ref))
            print("      ours   : %s" % ours)
            if theirs:
                print("      source : %s" % theirs)
        print("\nmatch: %d   not found: %d   differs: %d" % (ok, miss, diff))
        return
    ref = " ".join(a for a in sys.argv[1:] if not a.startswith("--"))
    t = lookup(ref)
    print(t if t else "not found: %r" % ref)


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main()
