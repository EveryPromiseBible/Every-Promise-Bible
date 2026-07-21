# -*- coding: utf-8 -*-
"""Populate the `verse` field of a promise batch from the local KJV.

WHY THIS EXISTS. `add_promises.py` already refuses any verse that is not
verbatim KJV, which is a good gate -- but it is a gate on work already done.
Whoever writes a batch still has to TYPE the verse, and typing scripture from
memory is exactly the failure this project cannot absorb. The gate then turns
every slip into a rejection to chase down by hand.

This inverts it. A batch author supplies only:

    {"reference": "Philippians 4:19", "meditations": [15 strings],
     "moods": ["Provision", "Anxious"]}

and the text is COPIED OUT OF THE SOURCE. Misquotation stops being a thing that
is caught and becomes a thing that cannot happen: nobody is quoting. The
add_promises check then passes trivially, which is the point -- it is left in
place as a second, independent lens rather than the only one.

Existing non-empty `verse` values are left alone unless --force, so a
deliberate EXCERPT (Matthew 28:20 quotes only the second half of its verse)
survives a re-run.

  python tools/fill_verses.py             # report what would be filled
  python tools/fill_verses.py --write     # fill and rewrite the batch files
  python tools/fill_verses.py --write --force   # overwrite existing verse text
"""
import json, os, sys, glob, io

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep
import kjv

BATCH_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "promises_new")


def main():
    ep.utf8_stdout()
    write = "--write" in sys.argv
    force = "--force" in sys.argv

    files = sorted(glob.glob(os.path.join(BATCH_DIR, "*.json")))
    if not files:
        print("no batches in %s" % BATCH_DIR)
        return

    filled = kept = unresolved = 0
    bad_refs = []

    for f in files:
        name = os.path.basename(f)
        batch = json.load(io.open(f, encoding="utf-8"))
        touched = False
        for p in batch:
            ref = (p.get("reference") or "").strip()
            have = (p.get("verse") or "").strip()
            if have and not force:
                kept += 1
                continue
            src = kjv.lookup(ref)
            if src is None:
                unresolved += 1
                bad_refs.append((name, ref))
                continue
            p["verse"] = src
            filled += 1
            touched = True
        if touched and write:
            with io.open(f, "w", encoding="utf-8") as fh:
                json.dump(batch, fh, ensure_ascii=False, indent=1)
        print("  %-30s %d entries" % (name, len(batch)))

    print("\nfilled %d   kept existing %d   UNRESOLVED %d" % (filled, kept, unresolved))
    for name, ref in bad_refs[:40]:
        print("  unresolved  %-26s %r" % (name, ref))
    if bad_refs:
        print("\nAn unresolved reference is usually a book-name spelling the ALIAS")
        print("table in kjv.py does not cover, or a verse that does not exist.")
    if not write:
        print("(dry run -- pass --write to apply)")


if __name__ == "__main__":
    main()
