# -*- coding: utf-8 -*-
"""Merge reviewed meditation batches back into PROMISES.

This pass rewrites MEDITATIONS ONLY. Everything else about a promise is frozen,
and the merge refuses rather than repairs if that is violated. The checks are
deliberately strict, because a review pass touching 22,830 lines across dozens
of concurrent reviewers is exactly the shape of edit that quietly loses content:

  SAME REFERENCE SET   no promise added, dropped, renamed or reordered
  VERSE FROZEN         byte-for-byte. A reviewer has no business editing
                       scripture while judging a devotional line, and the
                       corpus's headline claim is that all 1,522 are verbatim
                       KJV. Any change here is a bug, never an improvement.
  MOODS FROZEN         out of scope for this pass; a silent retag would be
                       invisible in the diff and would move the mood counts
  EXACTLY 15           the meditate deck renders a fixed stepper
  NO EMPTY / NO DUPE   within a promise

Reports the per-line diff so the size of the change is visible before it lands
-- a review that rewrites 8,000 lines is not a grace pass, it is a rewrite, and
should be caught by reading this number rather than by a reader noticing later.

  python tools/med_apply.py            # validate + show diff, write nothing
  python tools/med_apply.py --write
"""
import sys, os, io, json, glob

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep

REVIEW_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "med_review")


def main():
    ep.utf8_stdout()
    write = "--write" in sys.argv

    lines = ep.read_lines()
    _, P = ep.load(lines, "PROMISES")
    orig = {p["reference"]: p for p in P}

    files = sorted(glob.glob(os.path.join(REVIEW_DIR, "*.json")))
    if not files:
        print("no batches in %s" % REVIEW_DIR)
        return

    reviewed, problems = {}, []
    for f in files:
        name = os.path.basename(f)
        try:
            batch = json.load(io.open(f, encoding="utf-8"))
        except Exception as e:
            problems.append("%s UNREADABLE: %s" % (name, e))
            continue
        for p in batch:
            ref = p.get("reference")
            o = orig.get(ref)
            if o is None:
                problems.append("%s: unknown reference %r" % (name, ref))
                continue
            if ref in reviewed:
                problems.append("%s: %s reviewed twice" % (name, ref))
                continue
            if (p.get("verse") or "") != o["verse"]:
                problems.append("%s: %s VERSE CHANGED -- refusing" % (name, ref))
                continue
            if list(p.get("moods") or []) != list(o["moods"]):
                problems.append("%s: %s moods changed (frozen in this pass)" % (name, ref))
                continue
            meds = p.get("meditations") or []
            if len(meds) != 15:
                problems.append("%s: %s has %d meditations" % (name, ref, len(meds)))
                continue
            if any(not (m or "").strip() for m in meds):
                problems.append("%s: %s has an empty meditation" % (name, ref))
                continue
            if len(set(m.strip().lower() for m in meds)) != 15:
                problems.append("%s: %s has duplicate meditations" % (name, ref))
                continue
            reviewed[ref] = meds

    missing = set(orig) - set(reviewed)
    if missing:
        problems.append("%d promises were never reviewed (e.g. %s)"
                        % (len(missing), ", ".join(sorted(missing)[:5])))

    changed_lines = changed_promises = 0
    samples = []
    for ref, meds in reviewed.items():
        old = orig[ref]["meditations"]
        d = [(a, b) for a, b in zip(old, meds) if a != b]
        if d:
            changed_promises += 1
            changed_lines += len(d)
            if len(samples) < 25:
                samples.append((ref, d[0][0], d[0][1]))

    print("reviewed %d of %d promises" % (len(reviewed), len(orig)))
    print("changed  %d lines across %d promises (%.2f%% of all meditations)"
          % (changed_lines, changed_promises, 100.0 * changed_lines / (len(orig) * 15)))
    if samples:
        print("\nsample rewrites:")
        for ref, a, b in samples:
            print("   %-24s %s" % (ref, a))
            print("   %-24s -> %s" % ("", b))

    if problems:
        print("\n*** %d PROBLEMS ***" % len(problems))
        for pr in problems[:40]:
            print("   " + pr)

    if not write:
        print("\n(dry run -- pass --write to apply)")
        return
    if problems:
        print("\n*** REFUSING TO WRITE while any problem stands ***")
        sys.exit(1)

    for p in P:
        p["meditations"] = reviewed[p["reference"]]
    ep.dump_into(lines, "PROMISES", P)
    ep.write_lines(lines)

    _, P2 = ep.load(ep.read_lines(), "PROMISES")
    assert len(P2) == len(P)
    assert all(len(x["meditations"]) == 15 for x in P2)
    print("\n*** WROTE *** promises %d | meditations %d"
          % (len(P2), sum(len(x["meditations"]) for x in P2)))


if __name__ == "__main__":
    main()
