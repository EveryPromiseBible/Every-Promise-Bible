# -*- coding: utf-8 -*-
"""Fold recitative ὅτι -- the 'that' that sits immediately before a direct quote.

Greek uses ὅτι two ways. Before indirect speech it means "that" ("he said THAT
he would come"). But before DIRECT speech it is ὅτι recitativum: a quotation
marker with no English equivalent at all, the ancient equivalent of the opening
quotation mark itself. Rendering it "that" produces

    he said that “I am the one.”

which mixes indirect and direct speech and is not English. Matthew -- the book
that got the first full prose pass -- has zero of these. The rest of the corpus
had 55; the book agents folded 26 of them in passing, and this clears the rest.

The rule is deliberately narrow, because ὅτι before indirect speech is a REAL
"that" and must not be touched:

  * the unit's English is exactly "that" (no punctuation, no other words), and
  * its Greek is exactly ὅτι, and
  * the next unit carrying any English opens with a left double quote.

Anything else is left alone. Folding sets the English to "" -- the Greek stays
visible and clickable with its own tag, which is what folding means here and is
already the convention for particles and articles.

  python tools/fold_recitative.py            # dry run: list every fold
  python tools/fold_recitative.py --write
"""
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep

OPENERS = ("“", "‘")


def candidates(CH):
    for c in CH:
        for si, sec in enumerate(c["sections"]):
            ws = sec["words"]
            for j, w in enumerate(ws):
                if w[0].strip() != "that" or w[1].strip() != "ὅτι":
                    continue
                k = j + 1
                while k < len(ws) and not ws[k][0]:
                    k += 1
                if k < len(ws) and ws[k][0].lstrip().startswith(OPENERS):
                    yield c, si, j, ws, k


def main():
    ep.utf8_stdout()
    write = "--write" in sys.argv
    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS")

    found = list(candidates(CH))
    for c, si, j, ws, k in found:
        print("  %-18s S%-2d #%-4d  that -> (folded)   before %s"
              % (c["ref"], si, j, ws[k][0][:34]))
    print("\nrecitative hoti to fold: %d" % len(found))

    if not write:
        print("(dry run -- pass --write to apply)")
        return

    before_tokens = ep.total_tokens(CH)
    before_units = ep.total_units(CH)
    for c, si, j, ws, k in found:
        ws[j][0] = ""

    assert ep.total_tokens(CH) == before_tokens, "token count changed"
    assert ep.total_units(CH) == before_units, "unit count changed"

    ep.dump_into(lines, "CHAPTERS", CH)
    ep.write_lines(lines)
    _, C2 = ep.load(ep.read_lines(), "CHAPTERS")
    u, t = ep.total_units(C2), ep.total_tokens(C2)
    ok = u == ep.EXPECT_UNITS and t == ep.EXPECT_TOKENS
    left = len(list(candidates(C2)))
    print("\n*** WROTE *** units %d tokens %d %s | remaining: %d"
          % (u, t, "OK" if ok else "*** MISMATCH ***", left))
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
