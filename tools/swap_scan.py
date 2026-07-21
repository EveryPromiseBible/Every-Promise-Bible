# -*- coding: utf-8 -*-
"""Find neighbouring units whose English labels have been EXCHANGED or SHIFTED.

This is the defect class a prose read structurally cannot see. In every case the
English sentence is already correct, so nothing looks wrong; only the labels
underneath are attached to the wrong Greek words. Found in Luke 1 on 2026-07-20:

    Luke 1:35   τὸ γεννώμενον  labelled "the holy one"     <-- each is wearing
                ἅγιον          labelled "to be born"           the other's label
    Luke 1:64   ἀνεῴχθη        labelled "And immediately"
                παραχρῆμα      labelled "was opened"
    Luke 3:23   ἐτῶν / ὢν / υἱός  all slid one place left

Those were found by a human reading pairs in a band that happened to be flagged
as unaudited. There are ~73,000 pairs in the five hand-reordered books, so
reading them all is not a plan. But the damage has a SHAPE, and a shape can be
tested for.

THE TEST. gloss_scan already asks the loose question -- "does this English match
a NEIGHBOUR's definition?" -- and returns 712 hits corpus-wide, far too many to
read, because a loose cross-match happens all the time by chance (synonyms,
shared semantic fields, a verb and its object). So this tool asks the strict
question instead:

    unit A's English matches unit B's definition,
    AND unit B's English matches unit A's definition,
    AND neither matches its OWN definition.

Both directions at once, with both self-matches failing. Ordinary translation
choices do not produce mutual cross-matches by accident -- that is the signature
of two labels that have physically traded places.

SHIFT is the same idea run along a chain: A's English matches B's definition,
B's matches C's, and none matches its own. Two links are enough to be unusual;
the tool reports runs of 2 or more.

CALIBRATION. Tuned against the pre-audit baseline (71ca43e), where the known
defects still exist. Two parameters were set by measurement, not taste:

  WINDOW  Luke 1:64 traded labels across a distance of THREE units (ἀνεῴχθη at
          #86, παραχρῆμα at #89), so an adjacent-only test cannot see it.
          Widening the window catches it at 3. Measured on the baseline:
              window=1 -> 11 flags, misses 1:64
              window=3 -> 16 flags, catches 1:35 AND 1:64
              window=6 -> 20 flags, no further catches
          3 is where the recall is bought and the noise stops paying for itself.

  SCOPE   Restricted to words with a real dictionary meaning: verbs, nouns,
          adjectives, adverbs and pronouns. Articles, conjunctions and particles
          are excluded because their Strong's "definition" is a list of English
          particles, so neither side can ever produce an honest root match --
          that is lexicon formatting, not evidence. Including ADV/PRON costs
          only 3 extra flags corpus-wide and is what makes 1:64 reachable.

TWO KNOWN BLIND SPOTS -- this tool narrows the search, it does not close it:

  1. If the WRONG label is itself a stop word, there is nothing to match.
     Luke 1:65 (`τὰ ῥήματα` labelled "these") is invisible here for exactly
     that reason and was found by a human reading pairs.
  2. A thin lexicon entry causes false positives. Strong's G3793 ὄχλος is
     defined mostly by etymology ("from a derivative of...") and never contains
     the word "crowd", so the correct gloss "crowds" fails to match its own
     entry and the pair gets flagged. Expect a few of these.

  python tools/swap_scan.py              # whole corpus
  python tools/swap_scan.py "Luke"       # one book
  python tools/swap_scan.py --window 4   # widen the search
  python tools/swap_scan.py --shift      # only the shift test
"""
import sys, os, re, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep
import gloss_scan as gs

TAGRE = re.compile(r"(G\d+)")
WINDOW = 3


def checkable(morph):
    """Does this word have a real dictionary meaning to compare against?

    Verb/noun/adjective, plus adverbs and pronouns -- the latter two matter
    because Luke 1:64 traded an adverb's label with a verb's. Articles,
    conjunctions and particles are out: their Strong's entries are lists of
    English particles, so a root match is impossible either way.

    Note ART and ADV both start with 'A', as does the adjective tag A-NOM.
    Testing morph[0] alone silently classes every article as an adjective.
    """
    if not morph:
        return False
    if morph[0] in ("V", "N"):
        return True
    if morph == "A" or morph.startswith("A-"):
        return True
    return morph.startswith("ADV") or morph.startswith("PRON")


def unit_vocab(w, LEX):
    """Every definition word for every tag on this unit."""
    vocab = set()
    for t in (w[2] if len(w) > 2 else "").split("·"):
        m = TAGRE.match(t.strip())
        if m:
            vocab |= gs.ref_vocab(LEX.get(m.group(1)))
    return vocab


def unit_is_content(w):
    """Content word with a substantive gloss on both sides of the comparison."""
    if not w[1].strip() or not w[0].strip():
        return False
    tags = [t.strip() for t in (w[2] if len(w) > 2 else "").split("·") if t.strip()]
    if not tags:
        return False
    ok = False
    for t in tags:
        m = TAGRE.match(t)
        if not m:
            return False
        morph = t[len(m.group(1)):].strip()
        if morph and checkable(morph):
            ok = True
    return ok and bool(gs.content_toks(w[0]))


def profile(ws, LEX):
    """Per-unit (english content tokens, definition vocab, is-candidate)."""
    out = []
    for w in ws:
        if not unit_is_content(w):
            out.append((None, None, False))
            continue
        out.append((gs.content_toks(w[0]), unit_vocab(w, LEX), True))
    return out


def hits(eng, vocab):
    return bool(eng and vocab and gs.overlaps(eng, vocab))


def scan(CH, LEX, book=None, want_swap=True, want_shift=True, window=WINDOW):
    swaps, shifts = [], []
    for c in CH:
        if book and not (c["ref"] == book or re.sub(r" \d+$", "", c["ref"]) == book):
            continue
        for si, sec in enumerate(c["sections"]):
            ws = sec["words"]
            p = profile(ws, LEX)
            n = len(ws)

            if want_swap:
                for i in range(n - 1):
                    if not p[i][2] or hits(p[i][0], p[i][1]):
                        continue                     # absent, or already describes itself
                    for j in range(i + 1, min(n, i + 1 + window)):
                        if not p[j][2] or hits(p[j][0], p[j][1]):
                            continue
                        if hits(p[i][0], p[j][1]) and hits(p[j][0], p[i][1]):
                            swaps.append((c["ref"], si, i, ws[i], ws[j], j - i))

            if want_shift:
                run, i = [], 0
                while i < n - 1:
                    j = i + 1
                    if (p[i][2] and p[j][2] and not hits(p[i][0], p[i][1])
                            and hits(p[i][0], p[j][1])):
                        run.append(i)
                    else:
                        if len(run) >= 2:
                            shifts.append((c["ref"], si, run[0], [ws[k] for k in run + [run[-1] + 1]]))
                        run = []
                    i += 1
                if len(run) >= 2:
                    shifts.append((c["ref"], si, run[0], [ws[k] for k in run + [run[-1] + 1]]))
    return swaps, shifts


def main():
    ep.utf8_stdout()
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    book = args[0] if args else None
    only_shift = "--shift" in sys.argv
    only_swap = "--swap" in sys.argv

    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS")
    _, LEX = ep.load(lines, "LEXICON")

    window = WINDOW
    if "--window" in sys.argv:
        window = int(sys.argv[sys.argv.index("--window") + 1])
    swaps, shifts = scan(CH, LEX, book, want_swap=not only_shift,
                         want_shift=not only_swap, window=window)

    if swaps:
        print("=== EXCHANGED LABELS (each wears the other's) ===")
        for ref, si, i, a, b, dist in swaps:
            print("  %-16s S%-2d #%-4d  (%d apart)" % (ref, si, i, dist))
            print("       %-22s %r" % (a[1], a[0]))
            print("       %-22s %r" % (b[1], b[0]))
    if shifts:
        print("\n=== SHIFTED RUNS (labels slid one place) ===")
        for ref, si, i, units in shifts:
            print("  %-16s S%-2d #%-4d  (%d units)" % (ref, si, i, len(units)))
            for u in units:
                print("       %-22s %r" % (u[1], u[0]))

    print("\nexchanged-label pairs: %d" % len(swaps))
    print("shifted runs:          %d" % len(shifts))
    print("\nTriage, not a verdict -- read the pair before changing anything.")


if __name__ == "__main__":
    main()
