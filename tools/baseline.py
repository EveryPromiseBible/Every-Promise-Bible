# -*- coding: utf-8 -*-
"""Verify global invariants; optionally show a chapter's section layout.

Usage:
  python tools/baseline.py                 # invariant check
  python tools/baseline.py "Luke 7"        # + section layout for that chapter
"""
import sys
import epcore as ep


def main():
    ep.utf8_stdout()
    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS")
    _, LX = ep.load(lines, "LEXICON")
    _, PR = ep.load(lines, "PROMISES")
    _, AB = ep.load(lines, "ABBOTT")

    units, toks = ep.total_units(CH), ep.total_tokens(CH)
    print("blobs parse: CHAPTERS=%d LEXICON=%d PROMISES=%d ABBOTT=%d"
          % (len(CH), len(LX), len(PR), len(AB)))
    print("word units : %d (expect %d) %s" % (units, ep.EXPECT_UNITS,
          "OK" if units == ep.EXPECT_UNITS else "*** MISMATCH ***"))
    print("greek tokens: %d (expect %d) %s" % (toks, ep.EXPECT_TOKENS,
          "OK" if toks == ep.EXPECT_TOKENS else "*** MISMATCH ***"))

    if len(sys.argv) > 1:
        ref = sys.argv[1]
        ci = ep.chapter_index(CH, ref)
        print("\n=== %s is CHAPTERS[%d] ===" % (ref, ci))
        for si, s in enumerate(CH[ci]["sections"]):
            print("  §%d  units=%-4d tokens=%-4d  %s"
                  % (si, len(s["words"]), ep.section_tokens(s["words"]), s["heading"]))


if __name__ == "__main__":
    main()
