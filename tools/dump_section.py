# -*- coding: utf-8 -*-
"""Dump section units as `{index}|{english}|{greek}` for authoring a plan.

Usage:
  python tools/dump_section.py "Luke 7"        # list sections
  python tools/dump_section.py "Luke 7" 0      # dump section 0's units
"""
import sys
import epcore as ep


def main():
    ep.utf8_stdout()
    ref = sys.argv[1]
    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS")
    ci = ep.chapter_index(CH, ref)
    secs = CH[ci]["sections"]
    if len(sys.argv) < 3:
        for si, s in enumerate(secs):
            print("§%d  units=%-4d  %s" % (si, len(s["words"]), s["heading"]))
        return
    si = int(sys.argv[2])
    sec = secs[si]
    print("HEADING: %s | units: %d" % (sec["heading"], len(sec["words"])))
    print()
    for i, w in enumerate(sec["words"]):
        print("%3d | %-28s | %s" % (i, w[0], w[1]))


if __name__ == "__main__":
    main()
