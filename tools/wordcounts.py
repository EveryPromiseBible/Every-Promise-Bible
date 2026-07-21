# -*- coding: utf-8 -*-
"""Regenerate data/wordcounts.js -- the table shown in the introduction.

The introduction above Matthew 1 publishes, per book, the Greek word count in
this app beside the Greek word count in the SBLGNT source. That claim is the
whole basis for saying nothing was added to or taken from the Greek, so it must
never be typed by hand: it is computed from the corpus and checked against
MorphGNT every time this runs.

If a Greek word were ever lost or duplicated, this refuses to write and names
the book. That is deliberate -- a table that quietly reports a mismatch is worse
than no table, because the introduction presents it as proof.

RUN THIS AFTER ANY CHANGE TO THE GREEK. English-only edits cannot alter the
Greek column, but they do change the English column, so it is worth re-running
after those too.

  python tools/wordcounts.py            # check only, report
  python tools/wordcounts.py --write    # regenerate data/wordcounts.js
"""
import sys, os, re, io, json, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep

ORDER = ["Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians",
         "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians",
         "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus",
         "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John",
         "2 John", "3 John", "Jude", "Revelation"]
CODES = ["61-Mt", "62-Mk", "63-Lk", "64-Jn", "65-Ac", "66-Ro", "67-1Co", "68-2Co",
         "69-Ga", "70-Eph", "71-Php", "72-Col", "73-1Th", "74-2Th", "75-1Ti",
         "76-2Ti", "77-Tit", "78-Phm", "79-Heb", "80-Jas", "81-1Pe", "82-2Pe",
         "83-1Jn", "84-2Jn", "85-3Jn", "86-Jud", "87-Re"]
CODE = dict(zip(ORDER, CODES))
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "data", "wordcounts.js")


def sblgnt_tokens(book):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data",
                        "%s-morphgnt.txt" % CODE[book])
    with io.open(path, encoding="utf-8") as fh:
        return sum(1 for ln in fh if len(ln.split()) >= 7)


def build():
    _, CH = ep.load(ep.read_lines(), "CHAPTERS")
    grk, eng = collections.Counter(), collections.Counter()
    for c in CH:
        b = re.sub(r" \d+$", "", c["ref"])
        for s in c["sections"]:
            for w in s["words"]:
                grk[b] += len(w[1].split())
                eng[b] += len(w[0].split())
    rows, bad = [], []
    for b in ORDER:
        sb = sblgnt_tokens(b)
        if sb != grk[b]:
            bad.append((b, grk[b], sb))
        rows.append([b, grk[b], sb, eng[b]])
    return rows, bad


def main():
    ep.utf8_stdout()
    rows, bad = build()
    for b, g, s, e in rows:
        print("  %-18s greek %6d   sblgnt %6d   english %6d   %s"
              % (b, g, s, e, "ok" if g == s else "*** MISMATCH ***"))
    g = sum(r[1] for r in rows); s = sum(r[2] for r in rows); e = sum(r[3] for r in rows)
    print("  %-18s greek %6d   sblgnt %6d   english %6d   ratio %.2f"
          % ("TOTAL", g, s, e, float(e) / g))

    if bad:
        print("\n*** REFUSING TO WRITE -- the Greek does not match SBLGNT ***")
        for b, ours, theirs in bad:
            print("    %-18s ours %d, SBLGNT %d" % (b, ours, theirs))
        sys.exit(1)

    if "--write" not in sys.argv:
        print("\n(check only -- pass --write to regenerate data/wordcounts.js)")
        return
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("const WORDCOUNTS = " + json.dumps(rows, ensure_ascii=False) + ";\n")
    print("\nwrote %s" % OUT)


if __name__ == "__main__":
    main()
