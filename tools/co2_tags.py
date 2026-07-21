# -*- coding: utf-8 -*-
"""Resolve Strong's + morphology tags for 2 Corinthians words.

Priority: match each SBLGNT surface form against the app's OWN existing
tagged corpus (2 Cor shares almost all its vocabulary with the rest of the
NT, already tagged) -> inherit its exact 'G#### MORPH' tag. Fallback:
Strong's from the LEXICON by lemma (NFC-normalized), morph converted from
MorphGNT's parse code into the app's Robinson-style scheme and validated
against the codes the corpus actually uses. Nothing is invented.

Source Greek: SBLGNT via MorphGNT (tools/data/68-2Co-morphgnt.txt).

Usage:
  python tools/co2_tags.py 1            # chapter 1: coverage report
  python tools/co2_tags.py 1 --dump     # + every word as v|greek|G#### MORPH
  python tools/co2_tags.py 1 --json OUT  # write resolved words to OUT (json)
"""
import sys, os, json, collections, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep
import lex_build

# MorphGNT lemmatizes some deponents / variants differently from Strong's
# headwords (deponent -ομαι vs active headword, diacritic/breathing variants
# in the critical text vs Strong's TR spelling).  These Strong's numbers were
# each verified against the Abbott-Smith TEI (n="lemma|G#") and the Strong's
# Greek dictionary.  See tools/data/co2_lemma_overrides.json.
LEMMA_OVERRIDE = json.load(open(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "data",
                 "co2_lemma_overrides.json"), encoding="utf-8"))

# Well-formed morph codes 2 Cor introduces that the older corpus never used
# (perfect middle/passive indic., present passive subj.) — valid, not errors.
_WELLFORMED = __import__("re").compile(
    r"^(V-[PIFARLXY][AMP][ISOM]-[123][SP]|V-[PIFARL]F?[AMP][PN]|"
    r"[NA]-(NOM|GEN|DAT|ACC|VOC)|ART|PRON-(NOM|GEN|DAT|ACC|VOC)|"
    r"CONJ|PREP|ADV|PRT|INTJ|N|A|PRON)$")

MORPH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "68-2Co-morphgnt.txt")

def nfc(s):
    return unicodedata.normalize("NFC", s)

# MorphGNT parse code -> app Robinson-style morph -------------------------
TENSE = {"P":"P","I":"I","F":"F","A":"A","X":"R","Y":"L"}   # X=perfect->R, Y=pluperf->L
VOICE = {"A":"A","M":"M","P":"P"}
MOODF = {"I":"I","D":"M","S":"S","O":"O"}                    # D=imperative->M
CASE  = {"N":"NOM","G":"GEN","D":"DAT","A":"ACC","V":"VOC"}

def conv_morph(pos, parse):
    person, tense, voice, mood, case, number, gender, degree = list(parse)
    p2 = pos[0]
    if p2 == "V":
        t = TENSE.get(tense, tense); v = VOICE.get(voice, voice)
        if mood == "P":                      # participle: V-{T}{V}P (perfect uses PF)
            tt = "PF" if tense == "X" else t
            return "V-%s%sP" % (tt, v)
        if mood == "N":                      # infinitive: V-{T}{V}N
            return "V-%s%sN" % (t, v)
        m = MOODF.get(mood, mood)            # finite: V-{T}{V}{M}-{person}{number}
        return "V-%s%s%s-%s%s" % (t, v, m, person, number)
    if p2 == "N":
        return "N-%s" % CASE[case] if case in CASE else "N"
    if p2 == "A":
        return "A-%s" % CASE[case] if case in CASE else "A"
    if pos == "RA":
        return "ART"
    if p2 == "R":                            # RP/RR/RD/RI... pronouns
        return "PRON-%s" % CASE[case] if case in CASE else "PRON"
    if pos == "C-":
        return "CONJ"
    if pos == "P-":
        return "PREP"
    if pos == "D-":
        return "ADV"
    if pos == "X-":
        return "PRT"
    if pos == "I-":
        return "INTJ"
    return "?" + pos

# maps from the app's own data -------------------------------------------
def corpus_formmap(CH):
    m = collections.defaultdict(collections.Counter)
    for c in CH:
        for s in c["sections"]:
            for w in s["words"]:
                toks = w[1].split()
                tags = [t.strip() for t in w[2].split(" · ")] if w[2] else []
                if len(toks) == len(tags):
                    for tok, tag in zip(toks, tags):
                        m[nfc(tok)][tag] += 1
    return m

def corpus_morphset(CH):
    s = set()
    for c in CH:
        for sec in c["sections"]:
            for w in sec["words"]:
                for tag in w[2].split(" · "):
                    tag = tag.strip()
                    if tag:
                        s.add(tag.split(" ", 1)[1] if " " in tag else tag)
    return s

def lexicon_lemmamap(LEX):
    m = collections.defaultdict(list)
    for k, v in LEX.items():
        g = nfc((v.get("greek") or "").strip())
        if g:
            m[g].append(k)
    return m

def read_chapter(ch):
    tag = "08%02d" % ch
    with open(MORPH, encoding="utf-8") as f:
        for ln in f:
            p = ln.rstrip("\n").split(" ")
            if not p or not p[0].startswith(tag):
                continue
            yield p[0][4:6], p[4], p[6], p[1], p[2]   # verse, word, lemma, pos, parse

def strongs_lemmamap():
    """nfc(lemma) -> Strong's G#, from the Strong's Greek dictionary (same
    source the app's LEXICON is built from). First number wins."""
    m = {}
    for g, v in lex_build.build_lexicon().items():
        key = nfc((v.get("greek") or "").strip())
        if key and key not in m:
            m[key] = g
    return m

def resolve(ch, CH, LEX):
    fm = corpus_formmap(CH); lm = lexicon_lemmamap(LEX); mset = corpus_morphset(CH)
    sm = strongs_lemmamap()
    out = []
    for vv, word, lemma, pos, parse in read_chapter(ch):
        w = nfc(word); lem = nfc(lemma)
        if w in fm:
            tag = fm[w].most_common(1)[0][0]
            src = "form" if len(fm[w]) == 1 else "form*"
        else:
            morph = conv_morph(pos, parse)
            gs = lm.get(lem)                      # 1) app LEXICON lemma
            g = gs[0] if gs else None
            src = "lem"
            if not g and lem in LEMMA_OVERRIDE:    # 2) verified override
                g = LEMMA_OVERRIDE[lem]; src = "ovr"
            if not g:                              # 3) Strong's dict lemma
                g = sm.get(lem); src = "strd" if g else src
            if g:
                tag = "%s %s" % (g, morph)
                if morph not in mset and not _WELLFORMED.match(morph):
                    src += "!BADMORPH"
            else:
                tag = "?? %s" % morph
                src = "MISS"
        out.append({"v": vv, "greek": word, "lemma": lemma, "tag": tag, "src": src})
    return out

def main():
    ep.utf8_stdout()
    ch = int(sys.argv[1])
    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS"); _, LEX = ep.load(lines, "LEXICON")
    out = resolve(ch, CH, LEX)
    if "--json" in sys.argv:
        path = sys.argv[sys.argv.index("--json") + 1]
        with open(path, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=0)
    if "--dump" in sys.argv:
        for o in out:
            print("%s | %-15s | %-22s | %s" % (o["v"], o["greek"], o["tag"], o["src"]))
    srcs = collections.Counter(o["src"] for o in out)
    print("\n2 Cor %d: %d words | %s" % (ch, len(out), dict(srcs)))
    bad = [o for o in out if o["src"] in ("MISS", "lem!BADMORPH")]
    if bad:
        print("NEEDS ATTENTION:")
        for o in bad:
            print("  v%s %-15s lemma=%-14s %s" % (o["v"], o["greek"], o["lemma"], o["tag"]))

if __name__ == "__main__":
    main()
