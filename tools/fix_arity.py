# -*- coding: utf-8 -*-
"""Repair units where the Greek token count doesn't match the tag count.

A unit is [english, greek, tags]: tags are joined by ' · ', one per Greek token,
positionally. When a tag is missing the alignment silently shifts, so every tag
after the gap describes the WRONG word -- and the last word has no tag at all,
which means clicking it does nothing.

All 37 occurrences in this corpus are the same defect: a Greek ARTICLE carrying
no tag. 24 of them are in Matthew 1's genealogy ('τὸν Ἰωβὴδ' tagged only
'G5601 N-ACC'), which is the first chapter a reader opens.

The repair inserts 'G3588 ART' at the position of an untagged article. It is
applied only where doing so makes the counts match exactly, and only where the
token really is an article form -- anything else is reported and left alone,
because a mismatch with a different cause needs a human, not a guess.

  python tools/fix_arity.py            # dry run: show every repair
  python tools/fix_arity.py --write
"""
import re, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep

# Every inflected form of the Greek article.
ARTICLES = set("""ὁ ἡ τό τὸ τόν τὸν τήν τὴν τοῦ τῆς τῷ τῇ τά τὰ τούς τοὺς τάς τὰς
τῶν τοῖς ταῖς οἱ αἱ""".split())


def repair(unit):
    """Return (new_tags, note) or (None, reason) if we cannot safely repair."""
    toks = unit[1].split()
    tags = [t.strip() for t in (unit[2] if len(unit) > 2 else "").split("·") if t.strip()]
    if len(toks) == len(tags):
        return None, None
    gap = len(toks) - len(tags)
    if gap < 1:
        return None, "more tags than tokens"
    # Walk the tokens; wherever an untagged article can absorb the gap, insert.
    out, ti, inserted = [], 0, 0
    for tk in toks:
        if inserted < gap and tk in ARTICLES:
            # Does the tag at this position already describe an article?
            if ti < len(tags) and tags[ti].split()[1:2] == ["ART"]:
                out.append(tags[ti]); ti += 1
            else:
                out.append("G3588 ART"); inserted += 1
        else:
            if ti >= len(tags):
                return None, "ran out of tags at %r" % tk
            out.append(tags[ti]); ti += 1
    if inserted != gap or ti != len(tags):
        return None, "could not place %d missing tag(s)" % gap
    return " · ".join(out), "inserted %d article tag(s)" % inserted


def main():
    ep.utf8_stdout()
    write = "--write" in sys.argv
    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS")
    _, LEX = ep.load(lines, "LEXICON")
    assert "G3588" in LEX, "G3588 (the article) missing from LEXICON"

    fixed = skipped = 0
    for c in CH:
        for si, sec in enumerate(c["sections"]):
            for ui, w in enumerate(sec["words"]):
                toks = w[1].split()
                tags = [t.strip() for t in (w[2] if len(w) > 2 else "").split("·") if t.strip()]
                if not w[1].strip() or len(toks) == len(tags):
                    continue
                new, note = repair(w)
                if new is None:
                    print("  SKIP %-14s S%-2d #%-4d %-24s %s" % (c["ref"], si, ui, w[1], note))
                    skipped += 1
                    continue
                print("  %-14s S%-2d #%-4d %-24s %-30s -> %s"
                      % (c["ref"], si, ui, w[1], w[2], new))
                w[2] = new
                fixed += 1

    print("\nrepaired: %d   skipped: %d" % (fixed, skipped))

    # nothing but the tag string may have changed
    bad = [(c["ref"], ui) for c in CH for s in c["sections"] for ui, w in enumerate(s["words"])
           if len(w[1].split()) != len([t for t in w[2].split("·") if t.strip()]) and w[1].strip()]
    print("units still mismatched: %d" % len(bad))

    if write:
        ep.dump_into(lines, "CHAPTERS", CH)
        ep.write_lines(lines)
        l2 = ep.read_lines()
        _, C2 = ep.load(l2, "CHAPTERS")
        u, t = ep.total_units(C2), ep.total_tokens(C2)
        ok = u == ep.EXPECT_UNITS and t == ep.EXPECT_TOKENS
        print("\n*** WROTE *** units %d tokens %d %s" % (u, t, "OK" if ok else "*** MISMATCH ***"))
        if not ok:
            sys.exit(1)


if __name__ == "__main__":
    main()
