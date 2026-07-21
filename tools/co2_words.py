# -*- coding: utf-8 -*-
"""List the SBLGNT source words of a 2 Cor chapter, numbered, with morph tag
and a short gloss hint (from the app LEXICON), and dump them to JSON for the
assembler.  This is the backbone the paraphrase is authored against: every
word is anchored to one of these indices, so the Greek multiset stays exactly
SBLGNT.

Usage:
  python tools/co2_words.py 1            # print numbered words
  python tools/co2_words.py 1 --json     # also write tools/data/co2_words_1.json
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep, co2_tags as C

def build(ch):
    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS"); _, LEX = ep.load(lines, "LEXICON")
    words = []
    for k, o in enumerate(C.resolve(ch, CH, LEX)):
        g0 = o["tag"].split(" · ")[0].split(" ", 1)[0]
        defn = (LEX.get(g0, {}) or {}).get("definition", "") or ""
        gloss = " ".join(defn.replace(",", " ").split()[:6])
        words.append({"i": k, "v": o["v"], "greek": o["greek"], "tag": o["tag"], "gloss": gloss})
    return words

def main():
    ep.utf8_stdout()
    ch = int(sys.argv[1])
    words = build(ch)
    if "--json" in sys.argv:
        json.dump(words, open("tools/data/co2_words_%d.json" % ch, "w", encoding="utf-8"), ensure_ascii=False)
    cur = None
    for w in words:
        if w["v"] != cur:
            cur = w["v"]; print("  -- v%s --" % cur)
        print("  %3d  %-16s %-16s %s" % (w["i"], w["greek"], w["tag"], w["gloss"]))
    print("\n2 Cor %d: %d source words" % (ch, len(words)))

if __name__ == "__main__":
    main()
