# -*- coding: utf-8 -*-
"""Validate and merge new promise batches into PROMISES.

Batches are JSON files in tools/promises_new/, each a list of:

    {"reference": "Romans 8:1", "verse": "<verbatim KJV>",
     "meditations": [15 strings], "moods": ["Broken", "Confused"]}

Nothing merges until every entry passes. The checks exist because each one
guards a failure this project has already had somewhere:

  VERSE IS VERBATIM   The single rule that matters. The verse text must appear
                      in the KJV source exactly, contiguously. Not "close",
                      not modernised, not paraphrased -- a Bible app that
                      misquotes scripture is broken in the way that matters
                      most, and nothing downstream would catch it. Three such
                      misquotes were already found in the original 329.
  NO DUPLICATES       Against existing references AND across batches, so two
                      agents cannot both add Romans 8:28.
  EXACTLY 15          The existing 329 all carry exactly 15 meditations; a
                      batch with 14 would render a short deck silently.
  KNOWN MOODS ONLY    A typo'd mood ("Anxios") creates a pill that filters to
                      nothing, and the mood list is derived from the data.
  NO EMPTY / NO DUPE  within a promise's own meditations.

  python tools/add_promises.py                 # validate every batch, report
  python tools/add_promises.py --merge         # validate, then write
"""
import json, os, sys, glob, io, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep
import kjv

BATCH_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "promises_new")

MOODS = ["Encouraged", "Grateful", "Hopeful", "Anxious", "Peaceful", "Broken",
         "Confused", "Waiting", "Lonely", "Overwhelmed", "Joyful", "Tired",
         "Stressed", "Tempted", "Angry",
         # 2026-07-20: provision -- money, work, debt, lack, daily supply. The
         # UI derives its pill list from the data, so adding it here (the
         # validator's allow-list) is the only code change a new mood needs.
         "Provision",
         # 2026-07-21: healing REPLACES sick. "Sick" names a condition and asks
         # the reader to identify as it; "Healing" names what they are reaching
         # for. Same 116 promises, retagged by tools/retag_mood.py -- Sick is
         # deliberately absent from this list so a stale batch cannot reintroduce
         # it and quietly split the mood in two.
         "Healing"]


def span(ref):
    """(book, chapter, first_verse, last_verse) for overlap testing, or None."""
    return kjv.parse(ref)


def overlaps(a, b):
    """Do two references cover any verse in common?

    Reference-string equality is not enough. "1 Corinthians 15:54" and
    "1 Corinthians 15:54-55" are different keys carrying the same words, so the
    plain duplicate check waves both through and the app shows a reader the same
    verse twice under different headings. Comparing verse SPANS catches it
    exactly, where comparing text would need a fuzzy threshold and guess.
    """
    if not a or not b:
        return False
    return a[0] == b[0] and a[1] == b[1] and a[2] <= b[3] and b[2] <= a[3]


def check(p, seen, spans=None):
    """Return a list of problems for one promise; empty means it passes."""
    bad = []
    ref = (p.get("reference") or "").strip()
    if not ref:
        return ["no reference"]

    if spans is not None:
        mine = span(ref)
        for other_ref, other_span in spans.items():
            if other_ref.lower().replace(" ", "") == ref.lower().replace(" ", ""):
                continue
            if overlaps(mine, other_span):
                bad.append("verse span overlaps %s -- same text under two headings" % other_ref)
                break

    src = kjv.lookup(ref)
    if src is None:
        bad.append("reference does not resolve in KJV: %r" % ref)
    else:
        v = (p.get("verse") or "").strip()
        if not v:
            bad.append("empty verse")
        elif kjv._norm(v) not in kjv._norm(src):
            bad.append("VERSE NOT VERBATIM\n        ours  : %s\n        source: %s" % (v, src))

    key = ref.lower().replace(" ", "")
    if key in seen:
        bad.append("duplicate reference (already at %s)" % seen[key])

    meds = p.get("meditations") or []
    if len(meds) != 15:
        bad.append("%d meditations, need exactly 15" % len(meds))
    if any(not (m or "").strip() for m in meds):
        bad.append("empty meditation")
    if len(set(m.strip().lower() for m in meds)) != len(meds):
        bad.append("duplicate meditations within the promise")

    moods = p.get("moods") or []
    if not moods:
        bad.append("no moods")
    for m in moods:
        if m not in MOODS:
            bad.append("unknown mood %r (must be one of the 16)" % m)
    return bad


def prune():
    """Drop rejected entries from batch files so the clean remainder can merge.

    Batches are generated concurrently, so two agents can legitimately pick the
    same verse; whoever sorts first wins and the loser's entry is a duplicate
    through no fault of its own. --merge refuses while anything is rejected, so
    without this the whole run is blocked by a handful of collisions.

    Rewrites each file in place keeping only entries that pass, and reports what
    went. Deliberately separate from --merge: dropping content should be an
    explicit act, visible in its own output, not a silent step inside a write.
    """
    lines = ep.read_lines()
    _, P = ep.load(lines, "PROMISES")
    seen, spans = {}, {}
    for p in P:
        seen[p["reference"].lower().replace(" ", "")] = "existing"
        spans[p["reference"]] = span(p["reference"])

    dropped = 0
    for f in sorted(glob.glob(os.path.join(BATCH_DIR, "*.json"))):
        name = os.path.basename(f)
        batch = json.load(io.open(f, encoding="utf-8"))
        keep = []
        for p in batch:
            bad = check(p, seen, spans)
            if bad:
                print("  drop %-26s %-22s %s" % (name, p.get("reference", "?"),
                                                 bad[0].split("\n")[0][:70]))
                dropped += 1
                continue
            seen[p["reference"].lower().replace(" ", "")] = name
            spans[p["reference"]] = span(p["reference"])
            keep.append(p)
        if len(keep) != len(batch):
            with io.open(f, "w", encoding="utf-8") as fh:
                json.dump(keep, fh, ensure_ascii=False, indent=1)
        print("  %-28s kept %d of %d" % (name, len(keep), len(batch)))
    print("\ndropped %d entries; files rewritten" % dropped)


def main():
    ep.utf8_stdout()
    merge = "--merge" in sys.argv
    if "--prune" in sys.argv:
        prune()
        return

    lines = ep.read_lines()
    _, P = ep.load(lines, "PROMISES")
    seen, spans = {}, {}
    for p in P:
        seen[p["reference"].lower().replace(" ", "")] = "existing"
        spans[p["reference"]] = span(p["reference"])

    files = sorted(glob.glob(os.path.join(BATCH_DIR, "*.json")))
    if not files:
        print("no batches in %s" % BATCH_DIR)
        return

    accepted, rejected = [], 0
    for f in files:
        name = os.path.basename(f)
        try:
            batch = json.load(io.open(f, encoding="utf-8"))
        except Exception as e:
            print("  %-28s UNREADABLE: %s" % (name, e))
            rejected += 1
            continue
        good = 0
        for p in batch:
            bad = check(p, seen, spans)
            if bad:
                rejected += 1
                print("  REJECT %-22s %s" % (p.get("reference", "?"), "; ".join(bad)))
                continue
            seen[p["reference"].lower().replace(" ", "")] = name
            spans[p["reference"]] = span(p["reference"])
            accepted.append(p)
            good += 1
        print("  %-28s %d/%d ok" % (name, good, len(batch)))

    print("\naccepted: %d   rejected: %d   total after merge: %d"
          % (len(accepted), rejected, len(P) + len(accepted)))

    if not merge:
        print("(dry run -- pass --merge to write)")
        return
    if rejected:
        print("*** REFUSING TO MERGE while any entry is rejected ***")
        sys.exit(1)

    P.extend(accepted)
    ep.dump_into(lines, "PROMISES", P)
    ep.write_lines(lines)
    _, P2 = ep.load(ep.read_lines(), "PROMISES")
    _, CH = ep.load(ep.read_lines(), "CHAPTERS")
    print("\n*** WROTE *** promises %d | NT untouched: units %d tokens %d"
          % (len(P2), ep.total_units(CH), ep.total_tokens(CH)))
    assert ep.total_units(CH) == ep.EXPECT_UNITS and ep.total_tokens(CH) == ep.EXPECT_TOKENS


if __name__ == "__main__":
    main()
