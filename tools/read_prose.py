# -*- coding: utf-8 -*-
"""Render a chapter (or one section) as continuous English prose for a
readability read-through. Greek is ignored; blank-gloss (folded) units are
skipped so the output reads as running text.

Usage:
  python tools/read_prose.py "Acts 13"        # whole chapter, section by section
  python tools/read_prose.py "Acts 13" 2      # just section 2
"""
import sys
import epcore as ep


def render(sec):
    parts = [w[0] for w in sec["words"] if w[0] != ""]
    return " ".join(parts)


def main():
    ep.utf8_stdout()
    ref = sys.argv[1]
    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS")
    ci = ep.chapter_index(CH, ref)
    secs = CH[ci]["sections"]
    if len(sys.argv) >= 3:
        which = [int(sys.argv[2])]
    else:
        which = range(len(secs))
    for si in which:
        sec = secs[si]
        print("=== %s §%d — %s ===" % (ref, si, sec["heading"]))
        print(render(sec))
        print()


if __name__ == "__main__":
    main()
