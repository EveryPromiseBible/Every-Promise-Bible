# -*- coding: utf-8 -*-
"""Resolve Strong's + morphology tags for any NT book, book-parametric.

Generalizes the 2 Corinthians pipeline (co2_tags.py) to every book via the
BOOKS registry.  Priority for each SBLGNT word:
  1. match the surface form against the app's OWN already-tagged corpus
     (a new book shares almost all its vocabulary with the rest of the NT);
  2. app LEXICON lemma;
  3. verified per-book lemma override (data/<slug>_lemma_overrides.json);
  4. Strong's Greek dictionary lemma (same source the app LEXICON is built from).
Nothing is invented; well-formed perfect/passive morph codes new to the corpus
are accepted.

Greek source: SBLGNT via MorphGNT (tools/data/<NN>-<Bk>-morphgnt.txt).

Usage:
  python tools/nt_tags.py Ga 1            # coverage report
  python tools/nt_tags.py Ga 1 --dump     # + every word as v|greek|tag|src
"""
import sys, os, json, re, collections, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep
import lex_build

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

# Per-book config. code = 2-digit BBCCCVV book number; morph = MorphGNT file;
# ref = CHAPTERS ref prefix; after = chapter this book follows; slug = plan/
# override filename stem; chapters = chapter count.
BOOKS = {
    "2Co": {"code": "08", "morph": "68-2Co-morphgnt.txt", "ref": "2 Corinthians",
            "after": "1 Corinthians 16", "slug": "co2", "chapters": 13},
    "Ga":  {"code": "09", "morph": "69-Ga-morphgnt.txt", "ref": "Galatians",
            "after": "2 Corinthians 13", "slug": "ga", "chapters": 6},
    "Eph": {"code": "10", "morph": "70-Eph-morphgnt.txt", "ref": "Ephesians",
            "after": "Galatians 6", "slug": "eph", "chapters": 6},
    "Php": {"code": "11", "morph": "71-Php-morphgnt.txt", "ref": "Philippians",
            "after": "Ephesians 6", "slug": "php", "chapters": 4},
    "Col": {"code": "12", "morph": "72-Col-morphgnt.txt", "ref": "Colossians",
            "after": "Philippians 4", "slug": "col", "chapters": 4},
    "1Th": {"code": "13", "morph": "73-1Th-morphgnt.txt", "ref": "1 Thessalonians",
            "after": "Colossians 4", "slug": "th1", "chapters": 5},
    "2Th": {"code": "14", "morph": "74-2Th-morphgnt.txt", "ref": "2 Thessalonians",
            "after": "1 Thessalonians 5", "slug": "th2", "chapters": 3},
    "1Ti": {"code": "15", "morph": "75-1Ti-morphgnt.txt", "ref": "1 Timothy",
            "after": "2 Thessalonians 3", "slug": "ti1", "chapters": 6},
    "2Ti": {"code": "16", "morph": "76-2Ti-morphgnt.txt", "ref": "2 Timothy",
            "after": "1 Timothy 6", "slug": "ti2", "chapters": 4},
    "Tit": {"code": "17", "morph": "77-Tit-morphgnt.txt", "ref": "Titus",
            "after": "2 Timothy 4", "slug": "tit", "chapters": 3},
    "Phm": {"code": "18", "morph": "78-Phm-morphgnt.txt", "ref": "Philemon",
            "after": "Titus 3", "slug": "phm", "chapters": 1},
    "Heb": {"code": "19", "morph": "79-Heb-morphgnt.txt", "ref": "Hebrews",
            "after": "Philemon 1", "slug": "heb", "chapters": 13},
    "Jas": {"code": "20", "morph": "80-Jas-morphgnt.txt", "ref": "James",
            "after": "Hebrews 13", "slug": "jas", "chapters": 5},
    "1Pe": {"code": "21", "morph": "81-1Pe-morphgnt.txt", "ref": "1 Peter",
            "after": "James 5", "slug": "pe1", "chapters": 5},
    "2Pe": {"code": "22", "morph": "82-2Pe-morphgnt.txt", "ref": "2 Peter",
            "after": "1 Peter 5", "slug": "pe2", "chapters": 3},
    "1Jn": {"code": "23", "morph": "83-1Jn-morphgnt.txt", "ref": "1 John",
            "after": "2 Peter 3", "slug": "jn1", "chapters": 5},
    "2Jn": {"code": "24", "morph": "84-2Jn-morphgnt.txt", "ref": "2 John",
            "after": "1 John 5", "slug": "jn2", "chapters": 1},
    "3Jn": {"code": "25", "morph": "85-3Jn-morphgnt.txt", "ref": "3 John",
            "after": "2 John 1", "slug": "jn3", "chapters": 1},
    "Jud": {"code": "26", "morph": "86-Jud-morphgnt.txt", "ref": "Jude",
            "after": "3 John 1", "slug": "jud", "chapters": 1},
    "Rev": {"code": "27", "morph": "87-Re-morphgnt.txt", "ref": "Revelation",
            "after": "Jude 1", "slug": "rev", "chapters": 22},
}

def nfc(s):
    return unicodedata.normalize("NFC", s)

# MorphGNT parse code -> app Robinson-style morph -------------------------
TENSE = {"P": "P", "I": "I", "F": "F", "A": "A", "X": "R", "Y": "L"}
VOICE = {"A": "A", "M": "M", "P": "P"}
MOODF = {"I": "I", "D": "M", "S": "S", "O": "O"}
CASE  = {"N": "NOM", "G": "GEN", "D": "DAT", "A": "ACC", "V": "VOC"}

def conv_morph(pos, parse):
    person, tense, voice, mood, case, number, gender, degree = list(parse)
    p2 = pos[0]
    if p2 == "V":
        t = TENSE.get(tense, tense); v = VOICE.get(voice, voice)
        if mood == "P":
            tt = "PF" if tense == "X" else t
            return "V-%s%sP" % (tt, v)
        if mood == "N":
            return "V-%s%sN" % (t, v)
        m = MOODF.get(mood, mood)
        return "V-%s%s%s-%s%s" % (t, v, m, person, number)
    if p2 == "N":
        return "N-%s" % CASE[case] if case in CASE else "N"
    if p2 == "A":
        return "A-%s" % CASE[case] if case in CASE else "A"
    if pos == "RA":
        return "ART"
    if p2 == "R":
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

_WELLFORMED = re.compile(
    r"^(V-[PIFARLXY][AMP][ISOM]-[123][SP]|V-[PIFARL]F?[AMP][PN]|"
    r"[NA]-(NOM|GEN|DAT|ACC|VOC)|ART|PRON-(NOM|GEN|DAT|ACC|VOC)|"
    r"CONJ|PREP|ADV|PRT|INTJ|N|A|PRON)$")

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

def strongs_lemmamap():
    m = {}
    for g, v in lex_build.build_lexicon().items():
        key = nfc((v.get("greek") or "").strip())
        if key and key not in m:
            m[key] = g
    return m

def load_overrides(book):
    path = os.path.join(DATA, "%s_lemma_overrides.json" % BOOKS[book]["slug"])
    if os.path.exists(path):
        return json.load(open(path, encoding="utf-8"))
    return {}

def read_chapter(book, ch):
    cfg = BOOKS[book]
    tag = "%s%02d" % (cfg["code"], ch)
    with open(os.path.join(DATA, cfg["morph"]), encoding="utf-8") as f:
        for ln in f:
            p = ln.rstrip("\n").split(" ")
            if not p or not p[0].startswith(tag):
                continue
            yield p[0][4:6], p[4], p[6], p[1], p[2]   # verse, word, lemma, pos, parse

def resolve(book, ch, CH, LEX):
    fm = corpus_formmap(CH); lm = lexicon_lemmamap(LEX); mset = corpus_morphset(CH)
    sm = strongs_lemmamap(); ovr = load_overrides(book)
    out = []
    for vv, word, lemma, pos, parse in read_chapter(book, ch):
        w = nfc(word); lem = nfc(lemma)
        if w in fm:
            tag = fm[w].most_common(1)[0][0]
            src = "form" if len(fm[w]) == 1 else "form*"
        else:
            morph = conv_morph(pos, parse)
            gs = lm.get(lem)
            g = gs[0] if gs else None
            src = "lem"
            if not g and lem in ovr:
                g = ovr[lem]; src = "ovr"
            if not g:
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
    book = sys.argv[1]; ch = int(sys.argv[2])
    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS"); _, LEX = ep.load(lines, "LEXICON")
    out = resolve(book, ch, CH, LEX)
    if "--dump" in sys.argv:
        for o in out:
            print("%s | %-15s | %-22s | %s" % (o["v"], o["greek"], o["tag"], o["src"]))
    srcs = collections.Counter(o["src"] for o in out)
    print("\n%s %d: %d words | %s" % (BOOKS[book]["ref"], ch, len(out), dict(srcs)))
    bad = [o for o in out if "MISS" in o["src"] or "BADMORPH" in o["src"]]
    if bad:
        print("NEEDS ATTENTION:")
        for o in bad:
            print("  v%s %-16s lemma=%-16s %s" % (o["v"], o["greek"], o["lemma"], o["tag"]))

if __name__ == "__main__":
    main()
