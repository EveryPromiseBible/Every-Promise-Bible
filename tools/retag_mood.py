# -*- coding: utf-8 -*-
"""Rename a mood across every promise that carries it.

    python tools/retag_mood.py Sick Healing            # dry run, reports
    python tools/retag_mood.py Sick Healing --write    # actually writes

The UI derives its pill list from the data rather than a hardcoded array, so a
mood only exists as long as some promise carries it. Renaming is therefore a
data operation, not a code one -- there is no string in index.html to change.

Two things this guards that a find-and-replace would not:

  MERGE, DON'T DUPLICATE  If a promise already carries the destination mood,
                          renaming into it must not leave the mood listed twice.
                          The order of the remaining moods is preserved, because
                          it is the order they were authored in.
  NT UNTOUCHED            promises.js and chapters.js are written by the same
                          epcore dump path. The unit/token assertion at the end
                          is the same one add_promises.py makes: if a promise
                          edit ever perturbs the Greek, that is a catastrophe
                          worth failing loudly over rather than discovering
                          later.
"""
import os, sys, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep


def main():
    ep.utf8_stdout()
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    write = "--write" in sys.argv

    if len(args) != 2:
        print(__doc__)
        sys.exit(2)
    old, new = args

    lines = ep.read_lines()
    _, P = ep.load(lines, "PROMISES")

    touched, merged = 0, 0
    for p in P:
        moods = p.get("moods") or []
        if old not in moods:
            continue
        touched += 1
        if new in moods:
            # already carries the destination -- drop the old rather than
            # leaving the same mood twice
            p["moods"] = [m for m in moods if m != old]
            merged += 1
        else:
            p["moods"] = [new if m == old else m for m in moods]

    print("promises carrying %r: %d" % (old, touched))
    if merged:
        print("  of those, %d already had %r and were merged rather than renamed"
              % (merged, new))

    after = collections.Counter()
    for p in P:
        for m in (p.get("moods") or []):
            after[m] += 1
    print("\nmood distribution after retag (%d moods):" % len(after))
    for m, c in after.most_common():
        print("  %-14s %4d" % (m, c))

    if old in after:
        print("\n*** %r still present on %d promises ***" % (old, after[old]))

    if not write:
        print("\n(dry run -- pass --write to save)")
        return

    ep.dump_into(lines, "PROMISES", P)
    ep.write_lines(lines)

    fresh = ep.read_lines()
    _, P2 = ep.load(fresh, "PROMISES")
    _, CH = ep.load(fresh, "CHAPTERS")
    print("\n*** WROTE *** promises %d | NT untouched: units %d tokens %d"
          % (len(P2), ep.total_units(CH), ep.total_tokens(CH)))
    assert ep.total_units(CH) == ep.EXPECT_UNITS and ep.total_tokens(CH) == ep.EXPECT_TOKENS


if __name__ == "__main__":
    main()
