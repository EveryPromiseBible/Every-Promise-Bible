# -*- coding: utf-8 -*-
"""Print every Greek->English pair for a section, plus the joined prose.

This is the step that catches gloss drift: reading each pair confirms the
English still honestly describes the Greek beneath it. Importable + CLI.

Usage:
  python tools/pair_print.py "Luke 7" 0
"""
import sys
import epcore as ep

FOLD = "·(folded)"


def print_words(words):
    for j, w in enumerate(words):
        eng = w[0] if w[0] != "" else FOLD
        print("%3d | %-24s | %s" % (j, w[1], eng))


def prose(words):
    return " ".join(w[0] for w in words if w[0])


def main():
    ep.utf8_stdout()
    ref, si = sys.argv[1], int(sys.argv[2])
    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS")
    ci = ep.chapter_index(CH, ref)
    sec = CH[ci]["sections"][si]
    print("%s §%d — %s (%d units)" % (ref, si, sec["heading"], len(sec["words"])))
    print()
    print_words(sec["words"])
    print()
    print("=== PROSE ===")
    print(prose(sec["words"]))


if __name__ == "__main__":
    main()
