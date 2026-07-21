# -*- coding: utf-8 -*-
"""Assemble a 2 Corinthians chapter into the CHAPTERS blob from an authoring
module, guaranteeing the Greek multiset is exactly SBLGNT.

An authoring module (tools/plans/co2_<ch>.py) defines:

    CH = 1
    SECTIONS = [
      { "heading": "To the Church of God in Corinth",
        "notes": [],
        "units": [
            ("This is", []),          # supplied filler: english, no Greek
            ("Paul,", [0]),           # source word 0 with English
            ("our brother,", [11,12]),# bundle source words 11+12 (article+noun)
            ("", [3]),                # folded particle: Greek kept, no English
        ],
      },
      ...
    ]

Rules enforced:
  * every source index of the chapter is used exactly once across all units;
  * indices within a unit join their Greek (space) and tags (' · ') in the
    given order;
  * the resulting Greek token multiset equals SBLGNT for the chapter.

Usage:
  python tools/co2_assemble.py 1 --check     # verify only, print prose
  python tools/co2_assemble.py 1 --write     # insert/replace in index.html
"""
import sys, os, json, importlib.util, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep, co2_tags as C

REF = "2 Corinthians %d"
AFTER = "1 Corinthians 16"   # insert the book right after this chapter

def load_module(ch):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plans", "co2_%d.py" % ch)
    spec = importlib.util.spec_from_file_location("co2_%d" % ch, path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod

def assemble(ch, src):
    mod = load_module(ch)
    sections = []
    used = []
    for si, sec in enumerate(mod.SECTIONS):
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
    # coverage: each source index used exactly once
    dup = [i for i, n in collections.Counter(used).items() if n > 1]
    missing = [w["i"] for w in src if w["i"] not in set(used)]
    assert not dup, "source indices used more than once: %s" % dup[:20]
    assert not missing, "source indices never used: %s" % missing[:20]
    # multiset: assembled Greek == SBLGNT chapter Greek
    asm = collections.Counter(t for s in sections for w in s["words"] for t in w[1].split())
    sbl = collections.Counter(t for w in src for t in w["greek"].split())
    assert asm == sbl, "Greek multiset != SBLGNT (diff %s)" % \
        list((asm - sbl).items())[:10] + list((sbl - asm).items())[:10]
    return {"ref": REF % ch, "sections": sections}

def main():
    ep.utf8_stdout()
    ch = int(sys.argv[1])
    src = C.__dict__  # noqa
    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS"); _, LEX = ep.load(lines, "LEXICON")
    src = C.resolve(ch, CH, LEX)
    src = [{"i": k, "greek": o["greek"], "tag": o["tag"]} for k, o in enumerate(src)]
    chap = assemble(ch, src)
    nunits = sum(len(s["words"]) for s in chap["sections"])
    ntok = sum(len(w[1].split()) for s in chap["sections"] for w in s["words"])
    print("2 Cor %d assembled: %d sections, %d units, %d Greek tokens" %
          (ch, len(chap["sections"]), nunits, ntok))
    if "--check" in sys.argv:
        for s in chap["sections"]:
            print("\n### %s" % s["heading"])
            print(" ".join(w[0] for w in s["words"] if w[0]))
    if "--write" in sys.argv:
        # replace existing 2 Cor <ch> if present, else insert after AFTER
        idx = next((j for j, c in enumerate(CH) if c["ref"] == REF % ch), None)
        if idx is not None:
            CH[idx] = chap
        else:
            after = next(j for j, c in enumerate(CH) if c["ref"] == AFTER)
            # insert keeping chapters of this book in order
            ins = after + 1
            while ins < len(CH) and CH[ins]["ref"].startswith("2 Corinthians ") and \
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
