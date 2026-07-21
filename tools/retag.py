# -*- coding: utf-8 -*-
"""Correct wrong Strong's numbers on Greek tokens, corpus-wide.

The build gate was "every tag resolves to a LEXICON entry" (0 MISS). A tag that
resolves to the WRONG entry passes that check silently, so several ambiguous
forms carried a valid-but-wrong number and the popup showed a different word's
definition. tag_sense.py finds them; this applies the correction.

This tool touches ONLY the Strong's number inside a tag string. It never moves,
adds or removes a Greek token, never changes English, and never changes unit
counts -- and it asserts all of that before writing. The morphology suffix is
preserved exactly ("G3375 N-ACC" -> "G3376 N-ACC").

Each rule is (form_regex, old_tag, new_tag, why). The form regex must match the
WHOLE surface token, so a rule can never spread to a word it wasn't verified on.

Dry run by default; --write saves and re-checks the global invariants.

  python tools/retag.py
  python tools/retag.py --write
"""
import re, sys, os, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep

# Each entry verified individually against the Strong's dictionary, Abbott-Smith,
# and the actual English we used for that form everywhere it occurs.
RULES = [
    (r"δεῖ|δεῖν|ἔδει", "G1210", "G1163",
     "δεῖ 'it is necessary' was tagged δέω 'to bind'. MorphGNT lemmatises δεῖ to "
     "δέω (it is morphologically 3sg of δέω), so a lemma check cannot catch this; "
     "Strong's has a dedicated impersonal entry G1163. Clicking 'must' showed 'bind'."),

    # NOT ἱερά/ἱερὰ: those two occurrences (1 Cor 9:13 'the sacred things',
    # 2 Tim 3:15 'the sacred writings') are the genuine ADJECTIVE and are already
    # correctly tagged G2413. Including them here would have corrupted both.
    (r"ἱερῷ|ἱεροῦ|ἱερόν|ἱερὸν", "G2413", "G2411",
     "The NOUN ἱερόν 'temple' was tagged with the ADJECTIVE ἱερός 'holy'. "
     "Clicking 'temple' showed 'holy.'"),

    (r"εἰδὼς|εἰδώς|εἰδυῖα|εἰδότες|εἰδότε", "G3708", "G1492",
     "εἰδώς 'knowing' was tagged ὁράω 'to see'. The two verbs share a suppletive "
     "history but Strong's separates them; our gloss is always 'knowing'."),

    (r"μιᾷ|μιᾶς|μίαν|μία|μίᾳ", "G1519", "G1520",
     "The NUMERAL μία 'one' was tagged with the PREPOSITION εἰς 'into'. "
     "Strong's G3391 (feminine of εἷς) is absent from our LEXICON, so we point at "
     "G1520 εἷς, which is present and is where 53 of these already pointed."),

    (r"μῆνας|μῆνες|μηνὶ|μηνί|μηνῶν|μῆνα|μηνός", "G3375", "G3376",
     "μήν 'month' was tagged G3375 μήν '+ surely' -- a homograph particle that "
     "occurs once in the NT (Heb 6:14). Abbott-Smith keys the month entry as "
     "'μήν_2|G3376'. G3376 was absent from LEXICON and is added by this change."),
]

TAGRE = re.compile(r"^(G\d+)(.*)$", re.S)


def apply_rules(CH, verbose=True):
    changed = collections.Counter()
    for ch in CH:
        for sec in ch["sections"]:
            for w in sec["words"]:
                toks = w[1].split()
                tags = [t.strip() for t in (w[2] if len(w) > 2 else "").split("·")]
                if len(toks) != len(tags) or not w[1].strip():
                    continue
                out, hit = [], False
                for tk, tg in zip(toks, tags):
                    m = TAGRE.match(tg)
                    if m:
                        for pat, old, new, _ in RULES:
                            if m.group(1) == old and re.fullmatch(pat, tk):
                                tg = new + m.group(2)
                                changed[(old, new)] += 1
                                hit = True
                                break
                    out.append(tg)
                if hit:
                    w[2] = " · ".join(out)
    return changed


def main():
    ep.utf8_stdout()
    write = "--write" in sys.argv
    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS")
    _, LEX = ep.load(lines, "LEXICON")

    before_greek = [w[1] for c in CH for s in c["sections"] for w in s["words"]]
    before_en = [w[0] for c in CH for s in c["sections"] for w in s["words"]]

    changed = apply_rules(CH)

    after_greek = [w[1] for c in CH for s in c["sections"] for w in s["words"]]
    after_en = [w[0] for c in CH for s in c["sections"] for w in s["words"]]
    assert before_greek == after_greek, "*** GREEK CHANGED -- refusing ***"
    assert before_en == after_en, "*** ENGLISH CHANGED -- refusing ***"

    total = sum(changed.values())
    for (old, new), n in sorted(changed.items(), key=lambda kv: -kv[1]):
        why = next(r[3] for r in RULES if r[1] == old and r[2] == new)
        print("%s -> %s   %4d tokens\n    %s\n" % (old, new, n, why.split(".")[0] + "."))
    print("total retagged: %d" % total)

    missing = sorted({new for _, _, new, _ in RULES} - set(LEX))
    if missing:
        print("\n*** these target tags are ABSENT from LEXICON and must be added: %s"
              % ", ".join(missing))
        if write:
            sys.exit("refusing to write with a dangling tag target")

    if write:
        ep.dump_into(lines, "CHAPTERS", CH)
        ep.write_lines(lines)
        lines2 = ep.read_lines()
        _, CH2 = ep.load(lines2, "CHAPTERS")
        toks, units = ep.total_tokens(CH2), ep.total_units(CH2)
        ok = toks == ep.EXPECT_TOKENS and units == ep.EXPECT_UNITS
        print("\n*** WROTE *** units %d tokens %d %s"
              % (units, toks, "OK" if ok else "*** MISMATCH ***"))
        if not ok:
            sys.exit(1)


if __name__ == "__main__":
    main()
