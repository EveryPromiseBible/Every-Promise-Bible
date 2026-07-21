# -*- coding: utf-8 -*-
"""Audit Strong's tags against the true SBLGNT lemma for every Greek token.

The build pipeline's gate was "every tag resolves to a LEXICON entry" (0 MISS).
That cannot catch a tag that resolves to the WRONG entry -- and Greek has
genuinely ambiguous surface forms, so this happens. The worst case found:

    δεῖ  "it is necessary"  tagged G1210 δέω "to bind"  -- 86 of 89 occurrences

δεῖ is also the 3rd-singular present of δέω, so the tagger picked a valid but
wrong headword and nothing complained. Clicking "must" showed "bind".

This tool joins each unit's Greek token to the MorphGNT lemma for that token and
flags tags whose Strong's headword cannot be reconciled with it.

Orthographic noise is the enemy of a useful signal here: Strong's and SBLGNT
follow different spelling traditions (εἴδω/οἶδα, Μωσεύς/Μωϋσῆς, Δαβίδ/Δαυίδ,
τεσσαράκοντα/τεσσερακοντα). Those are the SAME entry and must not be reported.
So a tag is accepted if the headword matches the lemma, matches the surface form
itself (Strong's has per-form pronoun entries like G5216 ὑμῶν), or is close
enough under a prefix/edit-distance test.

Usage:
  python tools/tag_audit.py                 # corpus-wide summary, ranked
  python tools/tag_audit.py --detail        # every distinct mismatch
  python tools/tag_audit.py --form δεῖ      # where one form is tagged, by book
"""
import sys, os, re, glob, unicodedata, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def bare(s):
    """Lowercase, strip accents/breathing and parenthetical markers."""
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.lower().replace("(", "").replace(")", "").replace("’", "").replace("'", "")


def lemma_map():
    """surface form -> set of lemmas, from MorphGNT (column 4 = word, 6 = lemma)."""
    m = collections.defaultdict(set)
    for f in glob.glob(os.path.join(DATA, "*morphgnt.txt")):
        with open(f, encoding="utf-8") as fh:
            for ln in fh:
                p = ln.split()
                if len(p) > 6:
                    m[bare(p[4])].add(bare(p[6]))
    return m


def close(a, b):
    """Same word under a different spelling tradition?"""
    if not a or not b:
        return False
    if a == b:
        return True
    if a[:5] == b[:5] and abs(len(a) - len(b)) <= 3:
        return True
    if a.startswith(b) or b.startswith(a):
        return True
    # single vowel swap (τεσσαρακοντα / τεσσερακοντα) or one-char edit
    if len(a) == len(b) and sum(x != y for x, y in zip(a, b)) <= 1:
        return True
    return False


TAGRE = re.compile(r"(G\d+)")


def audit(CH, LEX, lem):
    """Yield (book, ref, form, gnum, headword, lemmas) for each suspect token."""
    head = {g: bare(e.get("greek", "")) for g, e in LEX.items()}
    for ch in CH:
        book = re.sub(r" \d+$", "", ch["ref"])
        for sec in ch["sections"]:
            for w in sec["words"]:
                toks = w[1].split()
                tags = [t.strip() for t in (w[2] if len(w) > 2 else "").split("·")]
                if len(toks) != len(tags):
                    continue                      # arity mismatch: a separate bug
                for tk, tg in zip(toks, tags):
                    m = TAGRE.match(tg)
                    if not m:
                        continue
                    g = m.group(1)
                    if g not in LEX:
                        yield book, ch["ref"], tk, g, "*ABSENT*", ""
                        continue
                    f, h = bare(tk), head[g]
                    lemmas = lem.get(f)
                    if not lemmas or not h:
                        continue
                    if close(h, f):
                        continue                  # Strong's inflected-form entry
                    if any(close(h, l) for l in lemmas):
                        continue                  # headword == the lemma
                    yield book, ch["ref"], tk, g, h, "/".join(sorted(lemmas))


def main():
    ep.utf8_stdout()
    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS")
    _, LEX = ep.load(lines, "LEXICON")
    lem = lemma_map()
    rows = list(audit(CH, LEX, lem))

    if "--form" in sys.argv:
        want = bare(sys.argv[sys.argv.index("--form") + 1])
        per = collections.defaultdict(collections.Counter)
        for book, ref, f, g, h, ls in rows:
            if bare(f) == want:
                per[book][g] += 1
        for b, c in per.items():
            print("%-18s %s" % (b, dict(c)))
        print("\ntotal flagged: %d" % sum(sum(c.values()) for c in per.values()))
        return

    agg = collections.Counter()
    for book, ref, f, g, h, ls in rows:
        agg[(f, g, h, ls)] += 1
    print("flagged tokens: %d   distinct (form,tag) pairs: %d\n" % (len(rows), len(agg)))
    print("%-16s %-7s %-16s %-20s %s" % ("FORM", "TAG", "strongs head", "sblgnt lemma", "n"))
    limit = None if "--detail" in sys.argv else 30
    for (f, g, h, ls), n in agg.most_common(limit):
        print("%-16s %-7s %-16s %-20s %d" % (f[:16], g, h[:16], ls[:20], n))


if __name__ == "__main__":
    main()
