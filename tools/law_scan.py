# -*- coding: utf-8 -*-
"""Find meditations shaped like LAW rather than grace.

`med_scan.py` catches vocabulary -- "strive", "earn", "sow/reap". This catches
SHAPE, which is the thing Chris actually noticed: a line can avoid every banned
word and still tell the reader what to do in order to get something from God.

Four shapes, in rough order of how badly they read:

  OBLIGATION   "you must", "your part", "God requires" -- duty stated outright
  CONDITIONAL  "if you X, He will Y" / "when you X, God Y" -- the reader's
               action is the hinge the promise turns on
  LEVER        "X unlocks/releases/activates/invites/moves God" -- softer, and
               the most common in this corpus. "Generosity unlocks overflow"
               says give-to-get without using either word.
  IMPERATIVE   a bare command to perform ("Guard your heart.", "Seek Him more.")

The last one needs the most care and is reported separately, because grace has
its OWN imperatives and they are welcome: rest, receive, believe, come, look,
remember, trust, lean. "Rest in His care." is on-frame. "Work at your faith."
is not. The allow-list below is what separates them, and it is the part most
likely to need tuning.

This is a TRIAGE list. The corpus is 22,830 lines; no regex settles whether one
is law. It says WHERE TO READ.

  python tools/law_scan.py                 # scan merged PROMISES
  python tools/law_scan.py --refs a.json   # limit to a reference list
  python tools/law_scan.py --csv out.csv   # dump hits for agent review
"""
import sys, os, io, re, json, csv, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep

OBLIGATION = [
    r"\byou must\b", r"\byou should\b", r"\byou need to\b", r"\byou have to\b",
    r"\byour part\b", r"\byour job\b", r"\byour responsibility\b",
    r"\brequires? you\b", r"\bexpects? you\b", r"\bdemands?\b",
    r"\bit is up to you\b", r"\bdo your\b", r"\bmake sure you\b",
]

CONDITIONAL = [
    r"\bif you\b[^.]{0,40}\b(he|god|the lord)\b[^.]{0,20}\bwill\b",
    r"\bwhen you\b[^.]{0,40}\b(he|god|the lord)\b[^.]{0,20}\b(will|gives|opens|responds)",
    r"\bas you\b[^.]{0,30}\b(he|god)\b[^.]{0,20}\b(will|gives)",
    r"\bthe more you\b", r"\bonly when you\b", r"\bunless you\b",
]

LEVER = [
    r"\bunlocks?\b", r"\bunleashe?s?\b", r"\bactivates?\b", r"\breleases\b",
    r"\bopens the door\b", r"\btriggers?\b", r"\binvites god\b",
    r"\bmoves god\b", r"\bmoves the hand\b", r"\bpositions? you (for|to receive)\b",
    r"\bqualifies you\b", r"\bearns? you\b", r"\bgets? you\b[^.]{0,15}\bfrom god\b",
]

# Bare command openings. Only flagged when the FIRST word is one of these and
# it is not on the grace allow-list.
GRACE_IMPERATIVES = {
    "rest", "receive", "believe", "trust", "come", "look", "remember", "lean",
    "know", "hear", "see", "let", "be", "breathe", "stop", "cease", "stay",
    "take", "hold", "run", "return", "lift", "raise", "sing", "rejoice",
    "give", "thank", "praise", "call", "ask", "speak", "say", "tell", "walk",
    "live", "love", "enjoy", "delight", "wait", "listen", "consider", "behold",
}

IMPERATIVE_START = re.compile(r"^([A-Z][a-z]+)\b")


# Same trap med_scan.py hit: the grace lens is usually expressed by NEGATING
# the law word, so "not your job" / "He does not require you steady" / "an
# invitation, not a demand" are the most on-frame lines in the corpus and a bare
# keyword search reports them as defects. 33 OBLIGATION hits, ~30 of them
# negations, before this.
NEGATED = [
    r"\bnot\b", r"\bn[o’']t\b", r"\bnever\b", r"\bno longer\b",
    r"\bwithout\b", r"\bnothing\b", r"\bfree(ly)?\b", r"\bgift\b",
    r"\bgrace\b", r"\balready\b", r"\binvitation\b", r"\brather than\b",
    r"\binstead of\b", r"\bhis word\b", r"\bhe (supplies|gives|met|took|came)\b",
]


def classify(m):
    low = m.lower()
    negated = any(re.search(p, low) for p in NEGATED)
    for pat in OBLIGATION:
        if re.search(pat, low) and not negated:
            return "OBLIGATION"
    for pat in CONDITIONAL:
        if re.search(pat, low):
            return "CONDITIONAL"
    for pat in LEVER:
        if re.search(pat, low):
            return "LEVER"
    return None


def imperative(m):
    """DISABLED -- see below. Always returns False.

    This tried to flag bare commands by matching the first capitalised word.
    It cannot work: "He stands with you." and "Guard your heart." are
    indistinguishable to a regex, because English marks the imperative by mood,
    not by form. The first run returned 15,198 "imperatives" across 885 "verbs",
    topped by he (3,508), his (1,751), your (1,582), the (1,220) -- i.e. it had
    found sentence-initial nouns and nothing else. Two thirds of the corpus
    flagged is not a triage list.

    Kept as a documented dead end so nobody rebuilds it. Imperative-vs-statement
    is a reading judgement; that is what the agent review pass is for.
    """
    return False


def main():
    ep.utf8_stdout()
    _, P = ep.load(ep.read_lines(), "PROMISES")

    hits = []
    imps = collections.Counter()
    imp_rows = []
    for p in P:
        for m in p["meditations"]:
            k = classify(m)
            if k:
                hits.append((k, p["reference"], m))
            else:
                w = imperative(m)
                if w:
                    imps[w] += 1
                    imp_rows.append((p["reference"], m, w))

    by_kind = collections.Counter(h[0] for h in hits)
    print("=== %d promises, %d meditations ===" % (
        len(P), sum(len(p["meditations"]) for p in P)))
    print("\nshape flags: %d   %s" % (len(hits), dict(by_kind)))
    for kind in ("OBLIGATION", "CONDITIONAL", "LEVER"):
        rows = [h for h in hits if h[0] == kind]
        if not rows:
            continue
        print("\n--- %s (%d) ---" % (kind, len(rows)))
        for _, ref, m in rows[:30]:
            print("   %-24s %s" % (ref, m))
        if len(rows) > 30:
            print("   ... %d more" % (len(rows) - 30))

    print("\n--- non-grace IMPERATIVE openings (%d lines, %d distinct verbs) ---"
          % (len(imp_rows), len(imps)))
    for w, n in imps.most_common(30):
        ex = next(m for r, m, v in imp_rows if v == w)
        print("   %-14s %4d   e.g. %s" % (w, n, ex))

    if "--csv" in sys.argv:
        out = sys.argv[sys.argv.index("--csv") + 1]
        with io.open(out, "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["kind", "reference", "meditation"])
            for k, r, m in hits:
                w.writerow([k, r, m])
            for r, m, v in imp_rows:
                w.writerow(["IMPERATIVE:" + v, r, m])
        print("\nwrote %d rows -> %s" % (len(hits) + len(imp_rows), out))


if __name__ == "__main__":
    main()
