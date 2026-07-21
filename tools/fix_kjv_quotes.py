# -*- coding: utf-8 -*-
"""Repair the 5 promise verses that are not verbatim KJV.

`kjv.py --verify` reported 1000 match / 5 differs against the 1,005 promises.
None was invented text, but four were silent MODERNISATIONS of KJV spelling
("show" for "shew") and one dropped clauses mid-verse without an ellipsis.

The modernisations matter because the corpus claims to be KJV and the reader
has no way to know a word was changed. The Ephesians one matters more: the
elision removed "even as God for Christ's sake hath forgiven you" -- the grace
clause that grounds the command. In a grace-centred Bible that is the half of
the verse you least want missing.

Matthew 28:20 stays an EXCERPT deliberately (the verse opens "Teaching them to
observe all things..."); only the spelling is corrected. Excerpting is a
sanctioned editorial choice here -- inventing a word is not.

  python tools/fix_kjv_quotes.py            # report
  python tools/fix_kjv_quotes.py --write    # apply
"""
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep
import kjv

# reference -> (exact old text, exact new text). Keyed on full text rather than
# a search-and-replace so a partial match cannot silently hit the wrong verse.
FIXES = {
    "Jeremiah 33:3": (
        "Call unto me, and I will answer thee, and show thee great and mighty things, which thou knowest not.",
        "Call unto me, and I will answer thee, and shew thee great and mighty things, which thou knowest not.",
    ),
    "3 John 1:2": (
        "Beloved, I wish above all things that thou mayest prosper and be in health, even as thy soul prospers.",
        "Beloved, I wish above all things that thou mayest prosper and be in health, even as thy soul prospereth.",
    ),
    "Matthew 28:20": (
        "And, lo, I am with you always, even unto the end of the world.",
        "And, lo, I am with you alway, even unto the end of the world.",
    ),
    # LORD is kept in small-caps styling (the source prints "Lord"); the check
    # folds case, so the only real defect is the colon.
    "Psalm 29:11": (
        "The LORD will give strength unto his people: the LORD will bless his people with peace.",
        "The LORD will give strength unto his people; the LORD will bless his people with peace.",
    ),
    "Ephesians 4:31-32": (
        "Let all bitterness, and wrath, and anger, and clamour, and evil speaking, be put away from you: and be ye kind one to another, tenderhearted, forgiving one another.",
        "Let all bitterness, and wrath, and anger, and clamour, and evil speaking, be put away from you, with all malice: And be ye kind one to another, tenderhearted, forgiving one another, even as God for Christ’s sake hath forgiven you.",
    ),
}


def main():
    ep.utf8_stdout()
    write = "--write" in sys.argv
    lines = ep.read_lines()
    _, P = ep.load(lines, "PROMISES")

    changed = 0
    for p in P:
        fix = FIXES.get(p["reference"])
        if not fix:
            continue
        old, new = fix
        if p["verse"].strip() != old:
            print("  SKIP %-20s text does not match expected old value" % p["reference"])
            print("       have: %s" % p["verse"][:90])
            continue
        src = kjv.lookup(p["reference"])
        if not kjv.faithful(new, src):
            print("  SKIP %-20s proposed text is still not verbatim" % p["reference"])
            continue
        p["verse"] = new
        changed += 1
        print("  fix  %-20s %s" % (p["reference"], new[:80]))

    print("\n%d of %d repaired" % (changed, len(FIXES)))
    if not write:
        print("(dry run -- pass --write to apply)")
        return
    if changed != len(FIXES):
        print("*** REFUSING TO WRITE: not every fix applied ***")
        sys.exit(1)

    ep.dump_into(lines, "PROMISES", P)
    ep.write_lines(lines)

    ok, miss, diff, _ = kjv.verify_existing()
    print("\n*** WROTE *** kjv verify -> match %d  not found %d  differs %d"
          % (ok, miss, diff))


if __name__ == "__main__":
    main()
