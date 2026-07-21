# -*- coding: utf-8 -*-
"""Generate and merge the new LEXICON/ABBOTT entries a book needs (Strong's
numbers not already in the app's blobs), built from the validated public-domain
parsers in lex_build.  Book-parametric; keeps each blob sorted by numeric
Strong's number and never alters an existing entry.

Usage:
  python tools/nt_lex.py Ga            # report new entries + anomaly scan
  python tools/nt_lex.py Ga --write    # merge them into index.html
"""
import sys, os, re, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep, nt_tags as T, lex_build as L

def gnum(k): return int(k[1:])

def collect(book, CH, LEX):
    nums = collections.OrderedDict()
    for ch in range(1, T.BOOKS[book]["chapters"] + 1):
        for o in T.resolve(book, ch, CH, LEX):
            for t in o["tag"].split(" · "):
                nums.setdefault(t.split(" ", 1)[0], True)
    return list(nums)

def main():
    ep.utf8_stdout()
    book = sys.argv[1]
    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS"); _, LEX = ep.load(lines, "LEXICON"); _, AB = ep.load(lines, "ABBOTT")
    nums = collect(book, CH, LEX)
    LB = L.build_lexicon(); ABB = L.build_abbott()
    new_lex = {g: LB[g] for g in nums if g not in LEX}
    new_ab  = {g: ABB[g] for g in nums if g not in AB and g in ABB}
    ab_skip = [g for g in nums if g not in AB and g not in ABB]
    print("%s: %d distinct G# | new LEXICON %d | new ABBOTT %d | ABBOTT-less %s"
          % (book, len(nums), len(new_lex), len(new_ab), ab_skip))
    sus = re.compile(r"participle|origin[a-z]|[a-z]{16,}")
    for g, v in new_lex.items():
        blob = v["definition"] + " || " + v["kjv"]
        if not v["greek"] or not v["definition"] or sus.search(blob):
            print("  LEX? %s %s: def=%r kjv=%r" % (g, v["greek"], v["definition"][:46], v["kjv"][:34]))
    for g, v in new_ab.items():
        if not v["lemma"]:
            print("  AB?  %s: no lemma" % g)
    if "--write" in sys.argv:
        lex_add = {k: v for k, v in new_lex.items() if k not in LEX}
        ab_add  = {k: v for k, v in new_ab.items()  if k not in AB}
        LEX2 = {k: (LEX.get(k) or lex_add.get(k)) for k in sorted(set(LEX) | set(lex_add), key=gnum)}
        AB2  = {k: (AB.get(k)  or ab_add.get(k))  for k in sorted(set(AB)  | set(ab_add),  key=gnum)}
        assert all(LEX2[k] == LEX[k] for k in LEX), "existing LEXICON entry changed"
        assert all(AB2[k] == AB[k] for k in AB), "existing ABBOTT entry changed"
        ep.dump_into(lines, "LEXICON", LEX2); ep.dump_into(lines, "ABBOTT", AB2)
        ep.write_lines(lines)
        l2 = ep.read_lines(); _, L3 = ep.load(l2, "LEXICON"); _, A3 = ep.load(l2, "ABBOTT")
        print("written & reloaded OK | LEXICON=%d ABBOTT=%d" % (len(L3), len(A3)))

if __name__ == "__main__":
    main()
