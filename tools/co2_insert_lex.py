# -*- coding: utf-8 -*-
"""Merge the new 2 Cor LEXICON/ABBOTT entries (tools/data/co2_new_*.json) into
index.html's blobs, keeping each blob sorted by numeric Strong's number (the
existing convention) and preserving every existing entry unchanged.

Idempotent: re-running only adds still-missing keys.  --dry reports without
writing.

Usage: python tools/co2_insert_lex.py [--dry]
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep

def gnum(k): return int(k[1:])

def main():
    ep.utf8_stdout()
    dry = "--dry" in sys.argv
    new_lex = json.load(open("tools/data/co2_new_lexicon.json", encoding="utf-8"))
    new_ab  = json.load(open("tools/data/co2_new_abbott.json",  encoding="utf-8"))
    lines = ep.read_lines()
    _, LEX = ep.load(lines, "LEXICON"); _, AB = ep.load(lines, "ABBOTT")
    lex_add = {k: v for k, v in new_lex.items() if k not in LEX}
    ab_add  = {k: v for k, v in new_ab.items()  if k not in AB}
    print("LEXICON: %d existing + %d new = %d" % (len(LEX), len(lex_add), len(LEX)+len(lex_add)))
    print("ABBOTT : %d existing + %d new = %d" % (len(AB), len(ab_add), len(AB)+len(ab_add)))
    LEX2 = {k: (LEX.get(k) or lex_add.get(k)) for k in sorted(set(LEX)|set(lex_add), key=gnum)}
    AB2  = {k: (AB.get(k)  or ab_add.get(k))  for k in sorted(set(AB)|set(ab_add),  key=gnum)}
    # sanity: existing values untouched
    assert all(LEX2[k] == LEX[k] for k in LEX), "existing LEXICON entry changed"
    assert all(AB2[k]  == AB[k]  for k in AB),  "existing ABBOTT entry changed"
    if dry:
        print("(dry run — not written)"); return
    ep.dump_into(lines, "LEXICON", LEX2)
    ep.dump_into(lines, "ABBOTT",  AB2)
    ep.write_lines(lines)
    # reload to confirm valid JSON round-trips
    lines2 = ep.read_lines()
    _, L3 = ep.load(lines2, "LEXICON"); _, A3 = ep.load(lines2, "ABBOTT")
    print("written & reloaded OK | LEXICON=%d ABBOTT=%d" % (len(L3), len(A3)))

if __name__ == "__main__":
    main()
