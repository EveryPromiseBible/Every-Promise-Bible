# -*- coding: utf-8 -*-
"""Mechanical prose defects: things a reader trips over that a script CAN see.

Most readability problems in this corpus have no signature -- "over all his
possessions he will put in charge him" is undetectable, because every gloss is
honest and every word present. Those need reading (see HANDOFF §9).

But a few classes DO have signatures, and they turned out to be the highest-value
finds of the Matthew prose pass, because no earlier audit caught them:

  duplicated adjacent words  "there there will be weeping"  (Mt 22:13, 24:51, 25:30)
                             "it was all it was all leavened" (Mt 13:33)
                             "collapse on on the way"       (Mt 15:34)
                             "I became to the weak weak"    (1 Cor 9:22)
  doubled speech verbs       "Peter answered him, said,"    (Mt 15:1, 19:27, 26:35)
  fragment after a stray cap "he healed them. So that the crowd was amazed"
  capital inside a quotation "'you fool!' Will be in danger" (Mt 5:22)

BEWARE false positives -- roughly half of each class is correct English:
  "the one who had had the legion"        past perfect, correct
  "those who sleep sleep at night"        participle + finite verb, correct (so does ESV)
  "we remember that that deceiver said"   conjunction + demonstrative, correct
So this is triage: it says where to look, not what to change. Read before fixing.

Usage:
  python tools/prose_scan.py                 # whole corpus
  python tools/prose_scan.py "Matthew"       # one book
  python tools/prose_scan.py --dup           # only one check
"""
import re, sys, os, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep

SPEECH = r"(said|says|answered|replied|declared|asked|cried|called)"

CHECKS = {
    "dup": ("duplicated adjacent word", re.compile(r"\b(\w+)\s+\1\b", re.I)),
    "speech": ("doubled speech verb", re.compile(r"\b%s\b[^.?!]{0,12},\s*%s," % (SPEECH, SPEECH), re.I)),
    "frag": ("fragment after sentence end", re.compile(r"[.!?]\s+(So that|Which|And which)\b")),
    # A capital after a closing quote is usually CORRECT -- the quotation ends and
    # a new sentence begins ("...blessing!” And every creature..."). Matching that
    # naively gives 524 hits, essentially all fine. The real defect (Mt 5:22
    # "'you fool!' Will be in danger") is a capitalised word that CONTINUES the
    # sentence, so only flag words that rarely open one.
    "quotecap": ("capital continuing a sentence after a closing quote",
                 re.compile(r"[!?]['’”]\s+"
                            r"(Will|Or|Is|Are|Was|Were|Shall|Should|Would|Can|Has|Have|Had"
                            r"|Of|To|In|With|From|Than|Nor|Because|Since)\b")),
}


def main():
    ep.utf8_stdout()
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    want = [k for k in CHECKS if "--" + k in sys.argv] or list(CHECKS)
    book = args[0] if args else None

    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS")
    counts = collections.Counter()

    for c in CH:
        if book and not (c["ref"] == book or re.sub(r" \d+$", "", c["ref"]) == book):
            continue
        for si, sec in enumerate(c["sections"]):
            prose = " ".join(w[0] for w in sec["words"] if w[0])
            for key in want:
                label, rx = CHECKS[key]
                for m in rx.finditer(prose):
                    counts[key] += 1
                    lo = max(0, m.start() - 55)
                    print("%-9s %-18s S%-2d ...%s..."
                          % (key, c["ref"], si, prose[lo:m.end() + 55].replace("\n", " ")))

    print()
    for k in want:
        print("%-9s %s: %d" % (k, CHECKS[k][0], counts[k]))
    print("\nTriage only -- about half of each class is correct English. Read before fixing.")


if __name__ == "__main__":
    main()
