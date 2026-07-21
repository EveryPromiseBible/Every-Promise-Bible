# -*- coding: utf-8 -*-
"""Split PROMISES into reviewable JSON batches for a grace-lens read.

The meditations live in `data/promises.js` as ONE line holding all 1,522
promises. Handing that to a reviewer -- human or agent -- is impossible, and
letting several reviewers edit it concurrently would corrupt it outright.

So the corpus is exported to numbered batches, reviewed in place, and merged
back by `med_apply.py`, which re-checks every invariant before writing. Same
shape as the promise-batch flow: nobody edits the blob directly.

  python tools/med_export.py            # default 40 promises per batch
  python tools/med_export.py --size 25
"""
import sys, os, io, json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep

REVIEW_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "med_review")


def main():
    ep.utf8_stdout()
    size = 40
    if "--size" in sys.argv:
        size = int(sys.argv[sys.argv.index("--size") + 1])

    _, P = ep.load(ep.read_lines(), "PROMISES")
    if not os.path.isdir(REVIEW_DIR):
        os.makedirs(REVIEW_DIR)

    n = 0
    for i in range(0, len(P), size):
        chunk = P[i:i + size]
        n += 1
        path = os.path.join(REVIEW_DIR, "rev%03d.json" % n)
        with io.open(path, "w", encoding="utf-8") as fh:
            json.dump(chunk, fh, ensure_ascii=False, indent=1)
    print("exported %d promises -> %d batches of %d in %s"
          % (len(P), n, size, REVIEW_DIR))


if __name__ == "__main__":
    main()
