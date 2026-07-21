# -*- coding: utf-8 -*-
"""Assemble any NT book's chapter into the CHAPTERS blob from an authoring
module, guaranteeing the Greek multiset equals SBLGNT.  Book-parametric
generalization of co2_assemble.py.

Authoring module: tools/plans/<slug>_<ch>.py defines
    CH = <ch>
    SECTIONS = [ { "heading": ..., "notes": [], "units": [ (english, [idxs]), ... ] }, ... ]
where each unit's indices are source-word indices (see nt_words.py); [] = a
supplied filler.  Every source index must be used exactly once; the assembled
Greek token multiset must equal SBLGNT.

Usage:
  python tools/nt_assemble.py Ga 1 --check     # verify + print prose
  python tools/nt_assemble.py Ga 1 --write     # insert/replace in index.html
"""
import sys, os, importlib.util, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep, nt_tags as T

def load_module(book, ch):
    slug = T.BOOKS[book]["slug"]
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plans", "%s_%d.py" % (slug, ch))
    spec = importlib.util.spec_from_file_location("%s_%d" % (slug, ch), path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod

def assemble(book, ch, src):
    mod = load_module(book, ch)
    sections = []; used = []
    for sec in mod.SECTIONS:
        words = []
        for en, idxs in sec["units"]:
            if not idxs:
                words.append([en, "", ""])
            else:
                greek = " ".join(src[i]["greek"] for i in idxs)
                tag = " · ".join(src[i]["tag"] for i in idxs)
                words.append([en, greek, tag])
                used.extend(idxs)
        sections.append({"heading": sec["heading"], "words": words, "notes": sec.get("notes", [])})
    dup = [i for i, n in collections.Counter(used).items() if n > 1]
    missing = [w["i"] for w in src if w["i"] not in set(used)]
    assert not dup, "source indices used more than once: %s" % dup[:20]
    assert not missing, "source indices never used: %s" % missing[:20]
    asm = collections.Counter(t for s in sections for w in s["words"] for t in w[1].split())
    sbl = collections.Counter(t for w in src for t in w["greek"].split())
    assert asm == sbl, "Greek multiset != SBLGNT (diff %s)" % \
        (list((asm - sbl).items())[:10] + list((sbl - asm).items())[:10])
    return {"ref": "%s %d" % (T.BOOKS[book]["ref"], ch), "sections": sections}

def main():
    ep.utf8_stdout()
    book = sys.argv[1]; ch = int(sys.argv[2])
    cfg = T.BOOKS[book]; ref = "%s %d" % (cfg["ref"], ch)
    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS"); _, LEX = ep.load(lines, "LEXICON")
    src = [{"i": k, "greek": o["greek"], "tag": o["tag"]}
           for k, o in enumerate(T.resolve(book, ch, CH, LEX))]
    chap = assemble(book, ch, src)
    nunits = sum(len(s["words"]) for s in chap["sections"])
    ntok = sum(len(w[1].split()) for s in chap["sections"] for w in s["words"])
    print("%s assembled: %d sections, %d units, %d Greek tokens" %
          (ref, len(chap["sections"]), nunits, ntok))
    if "--check" in sys.argv:
        for s in chap["sections"]:
            print("\n### %s" % s["heading"])
            print(" ".join(w[0] for w in s["words"] if w[0]))
    if "--write" in sys.argv:
        idx = next((j for j, c in enumerate(CH) if c["ref"] == ref), None)
        if idx is not None:
            CH[idx] = chap
        else:
            after = next(j for j, c in enumerate(CH) if c["ref"] == cfg["after"])
            ins = after + 1
            pref = cfg["ref"] + " "
            while ins < len(CH) and CH[ins]["ref"].startswith(pref) and \
                  int(CH[ins]["ref"].split()[-1]) < ch:
                ins += 1
            CH.insert(ins, chap)
        ep.dump_into(lines, "CHAPTERS", CH)
        ep.write_lines(lines)
        lines2 = ep.read_lines(); _, CH2 = ep.load(lines2, "CHAPTERS")
        print("written | total chapters=%d tokens=%d units=%d" %
              (len(CH2), ep.total_tokens(CH2), ep.total_units(CH2)))

if __name__ == "__main__":
    main()
