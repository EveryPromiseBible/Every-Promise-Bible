# -*- coding: utf-8 -*-
"""Apply a section reorder/gloss plan to index.html.

A plan is a small data module defining:
    CHAPTER = "Luke 7"          # chapter ref
    SECTION = 0                 # section index
    BLOCKS  = [ (a, b, [(src_idx, new_english_or_None), ...]), ... ]
each block covering a contiguous span [a,b) of the ORIGINAL section, reordered
into English order. new_english=None keeps the gloss; "" folds the unit
(Greek shown, English blank). Untouched spans are simply omitted.

Dry run (default): applies to memory, prints every Greek->English pair + prose,
checks the section's Greek multiset is unchanged. Writes nothing.
With --write: also saves index.html and re-checks the global token invariant.

Usage:
  python tools/apply_plan.py tools/plans/luke07_0.py
  python tools/apply_plan.py tools/plans/luke07_0.py --write
"""
import sys, os, importlib.util
import epcore as ep
import pair_print


LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plans", "APPLIED.log")


def applied_before(path):
    """Return the timestamp a plan was previously applied, or None.

    apply_plan's assertions verify the Greek multiset and the unit count are
    unchanged. Neither can see a plan landing on units that are no longer what
    its author read -- an overwrite preserves both. That is exactly how
    1 Corinthians 10:22 lost "Are we stronger than he?"; the spent plan
    1cor10_2fix.py was re-applied against shifted data and simply pasted the
    previous clause over ischyroteroi/autou. So the guard is a ledger, not an
    assertion: a plan is a one-shot instrument.
    """
    name = os.path.basename(path)
    if not os.path.exists(LEDGER):
        return None
    with open(LEDGER, encoding="utf-8") as fh:
        for line in fh:
            parts = line.strip().split("\t")
            if len(parts) >= 2 and parts[1] == name:
                return parts[0]
    return None


def record_applied(path):
    import datetime
    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write("%s\t%s\n" % (datetime.datetime.now().isoformat(timespec="seconds"),
                               os.path.basename(path)))


def load_plan(path):
    spec = importlib.util.spec_from_file_location("plan", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    ep.utf8_stdout()
    path = sys.argv[1]
    write = "--write" in sys.argv[2:]
    plan = load_plan(path)

    lines = ep.read_lines()
    _, CH = ep.load(lines, "CHAPTERS")
    ci = ep.chapter_index(CH, plan.CHAPTER)
    sec = CH[ci]["sections"][plan.SECTION]
    ws = [list(w) for w in sec["words"]]

    before = ep.tokset(ws)
    n_before = len(ws)
    for a, b, blk in plan.BLOCKS:
        ep.splice(ws, a, b, blk)
    after = ep.tokset(ws)

    assert before == after, "*** GREEK MULTISET CHANGED in section ***"
    assert len(ws) == n_before, "*** unit count changed in section ***"

    print("%s §%d — %s" % (plan.CHAPTER, plan.SECTION, sec["heading"]))
    print("units: %d (unchanged) | section tokens: %d | greek multiset unchanged: %s"
          % (len(ws), sum(after.values()), before == after))
    print()
    pair_print.print_words(ws)
    print()
    print("=== PROSE ===")
    print(pair_print.prose(ws))

    if write:
        already = applied_before(path)
        if already and "--force" not in sys.argv:
            print("\n*** REFUSED: this plan was already applied on %s ***" % already)
            print("Re-applying a spent plan is how 1 Corinthians 10:22 lost a whole")
            print("sentence: tools/plans/1cor10_2fix.py targeted indices 94/95 believing")
            print("them to be parazeloumen/ton kyrion, but by then they were")
            print("ischyroteroi/autou, and the assertions below cannot see that -- the")
            print("Greek multiset and unit count are both unchanged by an overwrite.")
            print("Pair-read the section first. Use --force only if you are certain.")
            sys.exit(2)
        sec["words"] = ws
        ep.dump_into(lines, "CHAPTERS", CH)
        ep.write_lines(lines)
        # re-load and verify the global invariant
        lines2 = ep.read_lines()
        _, CH2 = ep.load(lines2, "CHAPTERS")
        toks = ep.total_tokens(CH2)
        ok = toks == ep.EXPECT_TOKENS
        print("\n*** WROTE index.html *** global tokens: %d %s"
              % (toks, "OK" if ok else "*** MISMATCH ***"))
        if not ok:
            sys.exit(1)
        record_applied(path)


if __name__ == "__main__":
    main()
