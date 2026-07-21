# -*- coding: utf-8 -*-
"""List the SBLGNT source words of any NT book's chapter, numbered, with tag
and a short gloss hint — the backbone the paraphrase is authored against.
Book-parametric generalization of co2_words.py.

Usage:
  python tools/nt_words.py Ga 1            # print numbered words
  python tools/nt_words.py Ga 1 --json     # also write data/<slug>_words_1.json
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep, nt_tags as T

def build(book, ch):
    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS"); _, LEX = ep.load(lines, "LEXICON")
    words = []
    for k, o in enumerate(T.resolve(book, ch, CH, LEX)):
        g0 = o["tag"].split(" · ")[0].split(" ", 1)[0]
        defn = (LEX.get(g0, {}) or {}).get("definition", "") or ""
        gloss = " ".join(defn.replace(",", " ").split()[:6])
        words.append({"i": k, "v": o["v"], "greek": o["greek"], "tag": o["tag"], "gloss": gloss})
    return words

def main():
    ep.utf8_stdout()
    book = sys.argv[1]; ch = int(sys.argv[2])
    words = build(book, ch)
    if "--json" in sys.argv:
        slug = T.BOOKS[book]["slug"]
        json.dump(words, open("tools/data/%s_words_%d.json" % (slug, ch), "w", encoding="utf-8"), ensure_ascii=False)
    cur = None
    for w in words:
        if w["v"] != cur:
            cur = w["v"]; print("  -- v%s --" % cur)
        print("  %3d  %-16s %-16s %s" % (w["i"], w["greek"], w["tag"], w["gloss"]))
    print("\n%s %d: %d source words" % (T.BOOKS[book]["ref"], ch, len(words)))

if __name__ == "__main__":
    main()
