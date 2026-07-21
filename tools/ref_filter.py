# -*- coding: utf-8 -*-
"""Triage candidate promise references before any meditation is written.

Reference discovery is the cheap half of adding promises; writing 15 meditations
is the expensive half. So every candidate is screened FIRST against three things
that would make the work wasted:

  UNRESOLVED  the reference does not exist in the KJV (topical lists on the web
              really do cite verses that are not there -- a "Nehemiah 8:43" was
              caught last session in a chapter with 18 verses)
  EXISTING    the exact reference is already a promise
  OVERLAP     a DIFFERENT reference covering some of the same verses, e.g.
              "Psalm 34:10" vs "Psalm 34:8-10" -- same words, two headings,
              which is what add_promises.overlaps() rejects at merge time

Reads a plain text file of one reference per line (blank lines and #comments
ignored) and prints the clean survivors, ready to become a batch.

  python tools/ref_filter.py candidates.txt
  python tools/ref_filter.py candidates.txt --json out.json   # emit stubs
"""
import sys, os, io, json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep
import kjv
import add_promises as ap


def load_candidates(path):
    out = []
    with io.open(path, encoding="utf-8") as fh:
        for ln in fh:
            ln = ln.strip()
            if not ln or ln.startswith("#"):
                continue
            out.append(ln)
    return out


def main():
    ep.utf8_stdout()
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return
    cands = load_candidates(args[0])

    _, P = ep.load(ep.read_lines(), "PROMISES")
    existing_keys = {p["reference"].lower().replace(" ", "") for p in P}
    existing_spans = {p["reference"]: ap.span(p["reference"]) for p in P}

    good, seen_new = [], {}
    unresolved, dupe, overlap = [], [], []

    self_dupe = []
    for ref in cands:
        key = ref.lower().replace(" ", "")
        if kjv.lookup(ref) is None:
            unresolved.append(ref)
            continue
        if key in existing_keys:
            dupe.append(ref)
            continue
        # An EXACT repeat inside the candidate list. The span-overlap loop below
        # cannot catch this: it skips any comparison where the other reference
        # normalises to the same key, precisely so a reference is not reported
        # as overlapping itself. That guard means "Mark 10:30" listed twice --
        # easy when candidates are gathered under several mood headings -- sails
        # through and becomes two identical promises in two different batches.
        # Caught downstream by add_promises, but only after the expensive half
        # (15 meditations) had already been written for both.
        if key in {r.lower().replace(" ", "") for r in seen_new}:
            self_dupe.append(ref)
            continue
        mine = ap.span(ref)
        hit = None
        for other, sp in list(existing_spans.items()) + list(seen_new.items()):
            if other.lower().replace(" ", "") == key:
                continue
            if ap.overlaps(mine, sp):
                hit = other
                break
        if hit:
            overlap.append((ref, hit))
            continue
        seen_new[ref] = mine
        good.append(ref)

    print("candidates %d  ->  NEW %d | existing %d | overlap %d | unresolved %d"
          % (len(cands), len(good), len(dupe), len(overlap), len(unresolved)))
    if unresolved:
        print("\nUNRESOLVED (do not exist in KJV):")
        for r in unresolved:
            print("   ", r)
    if overlap:
        print("\nOVERLAP (same verses already covered under another heading):")
        for r, o in overlap[:60]:
            print("    %-24s <- %s" % (r, o))
    if dupe:
        print("\nalready a promise: %d" % len(dupe))

    print("\n--- %d NEW ---" % len(good))
    for r in good:
        print(r)

    if "--json" in sys.argv:
        out = sys.argv[sys.argv.index("--json") + 1]
        stubs = [{"reference": r, "verse": "", "meditations": [], "moods": []}
                 for r in good]
        with io.open(out, "w", encoding="utf-8") as fh:
            json.dump(stubs, fh, ensure_ascii=False, indent=1)
        print("\nwrote %d stubs -> %s" % (len(stubs), out))


if __name__ == "__main__":
    main()
