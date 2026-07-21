# -*- coding: utf-8 -*-
"""Emit the new LEXICON and ABBOTT entries 2 Corinthians needs (numbers not
already in the app's blobs), built from the validated public-domain parsers
in lex_build.  Writes staging JSON and flags any anomalous text so new
entries can be eyeballed before insertion.

Usage: python tools/co2_lex_emit.py
"""
import sys, os, json, collections, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep, co2_tags as C, lex_build as L

def main():
    ep.utf8_stdout()
    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS"); _, LEX = ep.load(lines, "LEXICON"); _, AB = ep.load(lines, "ABBOTT")
    nums = collections.OrderedDict()
    for ch in range(1, 14):
        for o in C.resolve(ch, CH, LEX):
            for t in o["tag"].split(" · "):
                nums.setdefault(t.split(" ", 1)[0], True)
    LB = L.build_lexicon(); ABB = L.build_abbott()
    new_lex = {g: LB[g] for g in nums if g not in LEX}
    new_ab  = {g: ABB[g] for g in nums if g not in AB and g in ABB}
    ab_skip = [g for g in nums if g not in AB and g not in ABB]
    json.dump(new_lex, open("tools/data/co2_new_lexicon.json", "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(new_ab,  open("tools/data/co2_new_abbott.json",  "w", encoding="utf-8"), ensure_ascii=False)
    print("new LEXICON:", len(new_lex), "| new ABBOTT:", len(new_ab), "| ABBOTT-less (match precedent):", ab_skip)
    # anomaly scan: mashed abbreviations / empty core fields
    sus = re.compile(r"participle|origin[a-z]|[a-z]{15,}")
    print("\n-- LEXICON anomaly scan --")
    for g, v in new_lex.items():
        blob = v["definition"] + " || " + v["kjv"] + " || " + v["derivation"]
        if not v["greek"] or not v["definition"] or sus.search(blob):
            print(f"  {g} {v['greek']}: def={v['definition'][:50]!r} kjv={v['kjv'][:40]!r}")
    print("-- ABBOTT anomaly scan --")
    for g, v in new_ab.items():
        if not v["lemma"] or not v["senses"] or not v["senses"][0]["text"]:
            print(f"  {g} {v['lemma']}: senses empty?")
    print("(scan complete)")

if __name__ == "__main__":
    main()
