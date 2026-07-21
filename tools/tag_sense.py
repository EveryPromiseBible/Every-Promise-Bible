# -*- coding: utf-8 -*-
"""Find Strong's tags whose DEFINITION never matches how the word is glossed.

Why this exists, and why tag_audit.py is not enough:

  δεῖ "it is necessary" is tagged G1210 δέω "to bind" in 89 of 92 places.
  Clicking "must" anywhere in the NT showed the definition of *bind*.

tag_audit.py cannot see this. It compares the tag's headword to the MorphGNT
lemma -- but MorphGNT itself lemmatizes δεῖ to δέω (all 92 occurrences), because
δεῖ is morphologically the 3rd-singular of δέω. The tag is consistent with the
lemma source and still wrong for the reader: Strong's has a dedicated entry
(G1163 δεῖ) for exactly this impersonal sense.

So this tool ignores lemmas and asks a different question: across every place a
given surface form carries a given tag, does the English we chose EVER share a
root with that tag's own definition? A form used 90 times whose gloss never once
matches its tag is a mistag, not a paraphrase. Aggregating over occurrences is
what makes the signal clean -- any single unit is noisy, but 90 consecutive
misses is not an accident.

Usage:
  python tools/tag_sense.py              # ranked suspects (n>=3)
  python tools/tag_sense.py --min 8      # only forms seen 8+ times
  python tools/tag_sense.py --show δεῖ   # every gloss used for one form
"""
import sys, os, re, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep
import gloss_scan as gs

TAGRE = re.compile(r"(G\d+)")


def collect(CH):
    """(form, gnum) -> list of the English glosses used for it."""
    seen = collections.defaultdict(list)
    for ch in CH:
        for sec in ch["sections"]:
            for w in sec["words"]:
                toks = w[1].split()
                tags = [t.strip() for t in (w[2] if len(w) > 2 else "").split("·")]
                if len(toks) != len(tags) or len(toks) != 1:
                    continue          # single-token units only: the gloss is unambiguous
                m = TAGRE.match(tags[0])
                if not m or not w[0].strip():
                    continue
                # Only content words: a function word's "definition" is a list of
                # English particles, and our gloss for it is usually a stop word,
                # so neither side can ever produce a root match. That is a
                # property of the lexicon's formatting, not a mistag.
                morph = tags[0][len(m.group(1)):].strip()
                if not morph or not gs.is_content(morph):
                    continue
                if not gs.content_toks(w[0]):
                    continue
                seen[(toks[0], m.group(1))].append((w[0], ch["ref"]))
    return seen


def main():
    ep.utf8_stdout()
    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS")
    _, LEX = ep.load(lines, "LEXICON")
    seen = collect(CH)

    if "--show" in sys.argv:
        want = sys.argv[sys.argv.index("--show") + 1]
        for (f, g), uses in sorted(seen.items()):
            if f == want:
                e = LEX.get(g, {})
                print("%s  %s  (%s = %s)" % (f, g, e.get("greek", "?"), str(e.get("kjv", ""))[:60]))
                for en, ref in uses[:40]:
                    print("    %-34s %s" % (en, ref))
        return

    lo = 3
    if "--min" in sys.argv:
        lo = int(sys.argv[sys.argv.index("--min") + 1])

    out = []
    for (f, g), uses in seen.items():
        if len(uses) < lo or g not in LEX:
            continue
        ref = gs.ref_vocab(LEX[g])
        if not ref:
            continue
        hits = sum(1 for en, _ in uses if gs.overlaps(gs.content_toks(en), ref))
        if hits == 0:
            out.append((len(uses), f, g, LEX[g].get("greek", ""),
                        str(LEX[g].get("kjv", ""))[:38], uses[0][0]))
    out.sort(reverse=True)
    print("forms whose gloss NEVER matches their tag's definition (n>=%d): %d\n" % (lo, len(out)))
    print("%-5s %-16s %-7s %-14s %-38s %s" % ("n", "form", "tag", "strongs", "kjv", "our gloss"))
    for n, f, g, gk, kjv, eg in out:
        print("%-5d %-16s %-7s %-14s %-38s %s" % (n, f[:16], g, gk[:14], kjv, eg[:26]))


if __name__ == "__main__":
    main()
