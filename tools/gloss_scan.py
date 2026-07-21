# -*- coding: utf-8 -*-
"""Automated gloss-honesty triage: flag Greek->English pairs that may have drifted.

The critical bug (HANDOFF.md): when units are reordered AND reglossed together,
an English label can slide onto the wrong Greek word. Nothing automated catches
it except reading pairs. This tool narrows what to read: for each CONTENT word
(verb / noun / adjective), it checks whether the English gloss shares any root
with that word's OWN Strong's/Thayer's definition + KJV. Zero overlap => suspect.

It is a TRIAGE, not a verdict: expect false positives (a paraphrase legitimately
uses words the lexicon doesn't). The point is to rank ~117k units down to a
few-hundred worth a human/subagent read.

Usage:
  python tools/gloss_scan.py "Matthew"        # one book, ranked flags
  python tools/gloss_scan.py --all             # every book: summary counts
  python tools/gloss_scan.py "Matthew" --soft  # also show soft flags
  python tools/gloss_scan.py "Matthew 8"       # a single chapter
"""
import sys, os, re, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep

STOP = set("""a an the of to in on at by for with and or but not no nor so as if then
than that this these those he his him she her it its they them their you your we us our
i my me is was are were be been being am has have had do did does will shall would should
may might can could must who whom which what where when why how there here all any some
one own out up off down over under into unto from about upon against before after also
even yet still now thus therefore because while though although since until per each
every both either neither more most much many few such very just only own too again
""".split())

# Fields that describe what the WORD means (not its parsing).
def ref_vocab(entry):
    if not entry:
        return set()
    txt = " ".join(str(entry.get(k, "")) for k in ("definition", "kjv", "derivation"))
    return toks(txt)

def toks(s):
    s = unicodedata.normalize("NFC", s or "").lower()
    return set(re.findall(r"[a-z]{2,}", s))

def content_toks(english):
    return [t for t in toks(english) if t not in STOP]

def stem_match(a, b):
    """True if two English tokens likely share a root."""
    if a == b:
        return True
    n = min(len(a), len(b))
    if n >= 4 and a[:4] == b[:4]:
        return True
    # one contains the other as a prefix (drove/driven etc. won't; but bless/blessed will)
    if len(a) >= 4 and (b.startswith(a) or a.startswith(b)):
        return True
    return False

def overlaps(eng_tokens, ref):
    for e in eng_tokens:
        for r in ref:
            if stem_match(e, r):
                return True
    return False

TAG = re.compile(r"^(G\d+)\s+([A-Z][A-Z0-9-]*)")

def is_content(morph):
    """Verb / noun / adjective => a word with a dictionary meaning to check.

    Careful: adjectives are tagged 'A-NOM' etc., but ART and ADV also start
    with 'A'. Testing morph[0] alone silently classes every article and adverb
    as an adjective -- which is how the first version of this tool counted 1,692
    'blank content words' that were really just folded articles.
    """
    return morph[0] in ("V", "N") or morph == "A" or morph.startswith("A-")

def scan_unit(english, greek, tags, LEX):
    """Return (flag_type, detail) or (None, None).
    flag_type: 'HARD' english content word matches none of its Greek defs;
               'SOFT' content Greek word glossed only by function words."""
    if not greek.strip():          # supplied filler: no Greek to match
        return None, None
    if not english.strip():        # folded particle: no English to check
        return None, None
    parts = [p.strip() for p in tags.split("·")]
    content_gnums = []
    for p in parts:
        m = TAG.match(p)
        if not m:
            continue
        g, morph = m.group(1), m.group(2)
        # V verb, N noun, A- adjective => content. Skip ART/ADV/CONJ/PREP/PRON/PRT.
        if is_content(morph):
            content_gnums.append(g)
    if not content_gnums:
        return None, None          # function-word-only unit: not this tool's job
    ref = set()
    for g in content_gnums:
        ref |= ref_vocab(LEX.get(g))
    et = content_toks(english)
    if not et:
        return "SOFT", "content word glossed only by function words"
    if overlaps(et, ref):
        return None, None
    return "HARD", "english %r shares no root with def of %s" % (english, ",".join(content_gnums))

def unit_content_gnums(tags):
    out = []
    for p in tags.split("·"):
        m = TAG.match(p.strip())
        if m and is_content(m.group(2)):
            out.append(m.group(1))
    return out

def unit_ref(tags, LEX):
    ref = set()
    for g in unit_content_gnums(tags):
        ref |= ref_vocab(LEX.get(g))
    return ref

WINDOW = 2  # how many neighbors on each side to compare against

def scan_chapter(chap, LEX):
    """Yield (section_idx, unit_idx, flag, english, greek, tags, detail).

    DRIFT (high signal): english shares no root with THIS word's definition but
      DOES match a neighbor's (within WINDOW) -- the label likely slid off its
      word. This is the fingerprint of the reorder+regloss bug.
    HARD (lower signal): no overlap with own def and no neighbor match either
      (often just paraphrase; skim only).
    SOFT: a content Greek word glossed entirely by function words.
    """
    for si, sec in enumerate(chap["sections"]):
        ws = sec["words"]
        for ui, w in enumerate(ws):
            eng, gk, tg = (w + ["", "", ""])[:3]
            ft, detail = scan_unit(eng, gk, tg, LEX)
            if not ft:
                continue
            if ft == "HARD":
                et = content_toks(eng)
                # does this english match a NEIGHBOUR's word-def better than its own?
                hit = None
                for dj in range(-WINDOW, WINDOW + 1):
                    if dj == 0:
                        continue
                    nj = ui + dj
                    if 0 <= nj < len(ws):
                        nref = unit_ref(ws[nj][2] if len(ws[nj]) > 2 else "", LEX)
                        if nref and overlaps(et, nref):
                            hit = (nj, ws[nj][1]); break
                if hit:
                    ft = "DRIFT"
                    detail = "english matches neighbor #%d %r, not own def" % (hit[0], hit[1])
            yield si, ui, ft, eng, gk, tg, detail

def book_of(ref):
    return re.sub(r" \d+$", "", ref)


def blank_content(CH):
    """Content words (V/N/A-) carrying NO English of their own.

    Folding is a sanctioned convention for particles and articles -- the Greek
    shows, the English is carried by a neighbour. Folding a VERB, NOUN or
    ADJECTIVE is different: that word has a dictionary meaning, and clicking it
    should say something. In the Mark audit every such unit in chs 13-16 turned
    out to be real drift (the word's meaning had slid onto a neighbouring
    particle), so this is a far higher-precision signal than the DRIFT
    heuristic. Numbers are the scariest case -- an unlabelled numeral is how
    Luke 3 lost a whole generation.
    """
    for c in CH:
        for si, sec in enumerate(c["sections"]):
            for ui, w in enumerate(sec["words"]):
                if w[0].strip() or not w[1].strip():
                    continue
                tags = w[2] if len(w) > 2 else ""
                for p in tags.split("·"):
                    m = TAG.match(p.strip())
                    if m and is_content(m.group(2)):
                        yield c["ref"], si, ui, w[1], tags
                        break

def main():
    ep.utf8_stdout()
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    show_soft = "--soft" in sys.argv
    do_all = "--all" in sys.argv
    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS")
    _, LEX = ep.load(lines, "LEXICON")

    if "--blank" in sys.argv:
        rows = list(blank_content(CH))
        want = args[0] if args else None
        if want:
            rows = [r for r in rows if book_of(r[0]) == want or r[0] == want]
        for ref, si, ui, gk, tg in rows:
            print("  %-16s §%d #%-4d %-24s %s" % (ref, si, ui, gk, tg))
        print("\n%d blank-English content-word units%s"
              % (len(rows), (" in " + want) if want else " corpus-wide"))
        return

    if do_all:
        from collections import defaultdict
        drift = defaultdict(int); hard = defaultdict(int); soft = defaultdict(int); units = defaultdict(int)
        for c in CH:
            b = book_of(c["ref"])
            for _, _, ft, *_ in scan_chapter(c, LEX):
                {"DRIFT": drift, "HARD": hard, "SOFT": soft}[ft][b] += 1
            units[b] += sum(len(s["words"]) for s in c["sections"])
        order = []
        seen = set()
        for c in CH:
            b = book_of(c["ref"])
            if b not in seen:
                seen.add(b); order.append(b)
        print("%-18s %8s %7s %7s %7s  %s" % ("BOOK", "units", "DRIFT", "hard", "soft", "DRIFT/1k"))
        td = th = ts = tu = 0
        for b in order:
            rate = 1000.0 * drift[b] / units[b] if units[b] else 0
            print("%-18s %8d %7d %7d %7d  %6.1f" % (b, units[b], drift[b], hard[b], soft[b], rate))
            td += drift[b]; th += hard[b]; ts += soft[b]; tu += units[b]
        print("%-18s %8d %7d %7d %7d  %6.1f" % ("TOTAL", tu, td, th, ts, 1000.0*td/tu if tu else 0))
        return

    target = args[0] if args else None
    if not target:
        print("give a book ('Matthew') or chapter ('Matthew 8'), or --all"); return
    chaps = [c for c in CH if c["ref"] == target or book_of(c["ref"]) == target]
    if not chaps:
        print("no match for", target); return
    nd = nh = ns = 0
    for c in chaps:
        rows = list(scan_chapter(c, LEX))
        driftrows = [r for r in rows if r[2] == "DRIFT"]
        hardrows = [r for r in rows if r[2] == "HARD"]
        softrows = [r for r in rows if r[2] == "SOFT"]
        nd += len(driftrows); nh += len(hardrows); ns += len(softrows)
        want = driftrows[:] + (hardrows if show_soft else []) + (softrows if show_soft else [])
        if not want:
            continue
        print("\n=== %s ===" % c["ref"])
        for si, ui, ft, eng, gk, tg, detail in driftrows:
            print("  DRIFT §%d #%-3d %-22s | %-26s | %s | %s" % (si, ui, gk, eng, tg, detail))
        if show_soft:
            for si, ui, ft, eng, gk, tg, detail in hardrows:
                print("  hard  §%d #%-3d %-22s | %-26s | %s" % (si, ui, gk, eng, tg))
            for si, ui, ft, eng, gk, tg, detail in softrows:
                print("  soft  §%d #%-3d %-22s | %-26s | %s" % (si, ui, gk, eng, tg))
    print("\n%s: %d DRIFT flags%s" % (target, nd, (", %d hard, %d soft" % (nh, ns)) if show_soft else ""))

if __name__ == "__main__":
    main()
