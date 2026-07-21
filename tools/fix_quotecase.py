# -*- coding: utf-8 -*-
"""Capitalise a quoted sentence that opens in lowercase.

    the prophet would be fulfilled: 'look, the virgin will become pregnant'

Found by spot-checking sections that book agents had declared clean, which is
the point: it is invisible to every tool we had. The earlier "lowercase
sentence-start" count looked for a lowercase word after a FULL STOP and found
exactly one, because these 38 all sit after an opening QUOTE instead.

All of them are in Matthew (13) and Romans (25) -- the two books that use the
single-quote convention, built before the rest of the corpus. That is the tell:
this is a convention artifact, not scattered typos.

The rule only fires where the quote genuinely begins a sentence: the preceding
visible character must be . ! ? or :, or the quote must open the section. A
quoted FRAGMENT mid-sentence ("he called it 'a den of robbers'") is correctly
lowercase and is left alone.

  python tools/fix_quotecase.py            # dry run
  python tools/fix_quotecase.py --write
"""
import sys, os, re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep

OPEN = "“‘'\""
# an opening quote, then a lowercase letter, at the very start of a gloss
LEAD = re.compile(r"^([%s]+\s*)([a-z])" % re.escape(OPEN))


def sweep(CH, apply=False):
    hits = []
    for c in CH:
        for si, sec in enumerate(c["sections"]):
            prev_end = None          # last visible char of the prose so far
            for w in sec["words"]:
                if not w[0]:
                    continue
                m = LEAD.match(w[0])
                if m and (prev_end is None or prev_end in ".!?:"):
                    new = w[0][:m.end(1)] + m.group(2).upper() + w[0][m.end(2):]
                    hits.append((c["ref"], si, w[0], new))
                    if apply:
                        w[0] = new
                s = w[0].rstrip()
                if s:
                    prev_end = s[-1]
    return hits


def main():
    ep.utf8_stdout()
    write = "--write" in sys.argv
    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS")

    before_u, before_t = ep.total_units(CH), ep.total_tokens(CH)
    hits = sweep(CH, apply=write)
    for ref, si, old, new in hits[:60]:
        print("  %-16s S%-2d %-30r -> %r" % (ref, si, old[:28], new[:28]))
    print("\nquoted sentences opening in lowercase: %d" % len(hits))

    if not write:
        print("(dry run -- pass --write to apply)")
        return

    assert ep.total_units(CH) == before_u and ep.total_tokens(CH) == before_t
    ep.dump_into(lines, "CHAPTERS", CH)
    ep.write_lines(lines)
    _, C2 = ep.load(ep.read_lines(), "CHAPTERS")
    u, t = ep.total_units(C2), ep.total_tokens(C2)
    ok = u == ep.EXPECT_UNITS and t == ep.EXPECT_TOKENS
    print("\n*** WROTE *** units %d tokens %d %s | remaining: %d"
          % (u, t, "OK" if ok else "*** MISMATCH ***", len(sweep(C2))))
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
