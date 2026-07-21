# -*- coding: utf-8 -*-
"""Reproduce the app's LEXICON and ABBOTT entries from their public-domain
sources, so new-vocabulary entries are byte-identical in format to the
existing ones.

Sources (downloaded into tools/data/):
  LEXICON <- strongsgreek.xml   (Strong's Greek Dict, StrongsGreekDictionaryXML_1.4)
  ABBOTT  <- abbott-smith.tei.xml (Abbott-Smith Manual Greek Lexicon, TEI)

Validation: parse each source, rebuild every G# that already exists in the
app's blob, and diff.  Only when existing entries reproduce exactly do we
trust the parser to mint new ones.

Usage:
  python tools/lex_build.py validate            # diff vs existing app entries
  python tools/lex_build.py show G728 G41 ...    # print rebuilt entries
"""
import sys, os, re, json, unicodedata, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep

HERE = os.path.dirname(os.path.abspath(__file__))
STRONGS_XML = os.path.join(HERE, "data", "strongsgreek.xml")
ABBOTT_XML  = os.path.join(HERE, "data", "abbott-smith.tei.xml")

def nfc(s): return unicodedata.normalize("NFC", s)
def ws(s):  return re.sub(r"\s+", " ", s).strip()

# ---------- LEXICON (Strong's) ------------------------------------------
def _render_strongs(frag):
    # <strongsref ... strongs="25"/> -> (G25); drop <see/>; strip other tags
    frag = re.sub(r'<strongsref[^>]*strongs="0*(\d+)"[^>]*/>', r'(G\1)', frag)
    frag = re.sub(r'<see[^>]*/>', '', frag)
    frag = re.sub(r'<[^>]+>', '', frag)
    return ws(frag)

def _rebalance(deriv, defn):
    """Strong's XML sometimes ends <strongs_derivation> mid-parenthetical and
    the balancing text spills into <strongs_def>.  Pull it back so derivation
    parens close, matching how the app stores these."""
    opened = deriv.count("(") - deriv.count(")")
    if opened <= 0 or not defn:
        return deriv, defn
    bal, i = opened, 0
    while i < len(defn) and bal > 0:
        if defn[i] == "(": bal += 1
        elif defn[i] == ")": bal -= 1
        i += 1
    while i < len(defn) and defn[i] in ";:":  # trailing separator stays with deriv
        i += 1
    moved, rest = defn[:i].strip(), defn[i:].strip()
    return ws(deriv + " " + moved), rest

def build_lexicon():
    x = open(STRONGS_XML, encoding="utf-8").read()
    out = {}
    for m in re.finditer(r'<entry strongs="0*(\d+)">(.*?)</entry>', x, re.S):
        num, body = m.group(1), m.group(2)
        g = re.search(r'<greek\b[^>]*\bunicode="([^"]*)"[^>]*\btranslit="([^"]*)"', body)
        if not g:
            g2 = re.search(r'<greek\b[^>]*\btranslit="([^"]*)"[^>]*\bunicode="([^"]*)"', body)
            greek, translit = (g2.group(2), g2.group(1)) if g2 else ("", "")
        else:
            greek, translit = g.group(1), g.group(2)
        pr = re.search(r'<pronunciation\b[^>]*\bstrongs="([^"]*)"', body)
        pron = pr.group(1) if pr else ""
        der = re.search(r'<strongs_derivation>(.*?)</strongs_derivation>', body, re.S)
        deriv = _render_strongs(der.group(1)) if der else ""
        de = re.search(r'<strongs_def>(.*?)</strongs_def>', body, re.S)
        defn = _render_strongs(de.group(1)) if de else ""
        deriv, defn = _rebalance(deriv, defn)
        kj = re.search(r'<kjv_def>(.*?)</kjv_def>', body, re.S)
        kjv = _render_strongs(kj.group(1)) if kj else ""
        kjv = re.sub(r'^:--\s*', '', kjv)
        out["G"+num] = {"greek": greek, "translit": translit, "pronunciation": pron,
                        "derivation": deriv, "definition": defn, "kjv": kjv}
    return out

# ---------- ABBOTT (Abbott-Smith TEI) -----------------------------------
import xml.etree.ElementTree as ET

def _local(tag): return tag.rsplit("}", 1)[-1]

def _esc(s):  # ElementTree decodes entities; the app stores them escaped
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def wse(s): return ws(_esc(s))

def _flat(el, skip_sense=False):
    """Flatten inline content to text; optionally skip nested <sense>."""
    parts = []
    if el.text: parts.append(el.text)
    for c in el:
        if skip_sense and _local(c.tag) == "sense":
            if c.tail: parts.append(c.tail)
            continue
        parts.append(_flat(c))
        if c.tail: parts.append(c.tail)
    return "".join(parts)

def _sense(el):
    node = {"num": (el.get("n") or "").strip(), "text": wse(_flat(el, skip_sense=True))}
    subs = [_sense(c) for c in el if _local(c.tag) == "sense"]
    node["subsenses"] = subs
    return node

def _abbott_entry(entry_xml):
    el = ET.fromstring(entry_xml)
    n = el.get("n") or ""
    lemma = n.split("|", 1)[0]
    rec = {"lemma": lemma}
    occ = el.find(".//{*}note[@type='occurrencesNT']")
    occ_txt = wse(_flat(occ)) if occ is not None else ""
    rec["occurrencesNT"] = None if (occ is None or "(KJV)" in occ_txt) else occ_txt
    form = el.find("{*}form")
    rec["form"] = wse(_flat(form)) if form is not None else ""
    etym = el.find("{*}etym")
    rec["etymology"] = wse(_flat(etym)) if etym is not None else ""
    rec["senses"] = [_sense(c) for c in el if _local(c.tag) == "sense"]
    re_el = el.find("{*}re")
    rec["synonyms"] = wse(_flat(re_el)) if re_el is not None else ""
    return n, rec

def build_abbott():
    x = open(ABBOTT_XML, encoding="utf-8").read()
    out = {}
    for m in re.finditer(r'<entry\b.*?</entry>', x, re.S):
        try:
            n, rec = _abbott_entry(m.group(0))
        except ET.ParseError:
            continue
        gs = re.findall(r'\|G(\d+)', n)
        for g in gs:
            out["G"+g] = rec
    return out

if __name__ == "__main__":
    ep.utf8_stdout()
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if cmd in ("validate", "validate-lex"):
        lines = ep.read_lines(); _, LEX = ep.load(lines, "LEXICON")
        built = build_lexicon()
        miss = bad = 0
        for k, v in LEX.items():
            if k not in built: miss += 1; continue
            if built[k] != v:
                bad += 1
                if bad <= 8:
                    for f in v:
                        if v[f] != built[k].get(f):
                            print(f"{k}.{f}\n  app  : {v[f]!r}\n  built: {built[k].get(f)!r}")
        print(f"\nLEXICON: {len(LEX)} app entries | {miss} absent in source | {bad} mismatched")
    if cmd in ("validate", "validate-ab"):
        lines = ep.read_lines(); _, AB = ep.load(lines, "ABBOTT")
        built = build_abbott()
        miss = bad = 0; shown = 0
        for k, v in AB.items():
            if k not in built: miss += 1; continue
            if built[k] != v:
                bad += 1
                if shown < 6:
                    shown += 1
                    print(f"--- {k} ---")
                    for f in ["lemma","occurrencesNT","form","etymology","synonyms"]:
                        if v.get(f) != built[k].get(f):
                            print(f"  {f}\n    app  : {v.get(f)!r}\n    built: {built[k].get(f)!r}")
                    if v.get("senses") != built[k].get("senses"):
                        print(f"  senses app  : {json.dumps(v.get('senses'),ensure_ascii=False)[:300]}")
                        print(f"  senses built: {json.dumps(built[k].get('senses'),ensure_ascii=False)[:300]}")
        print(f"\nABBOTT: {len(AB)} app entries | {miss} absent in source | {bad} mismatched")
