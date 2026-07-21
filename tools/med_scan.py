# -*- coding: utf-8 -*-
"""Scan meditations for the defects `add_promises.py` structurally cannot see.

add_promises validates SHAPE -- 15 of them, none empty, none duplicated, verse
verbatim, moods known. All of that can pass while the content is wrong in the
two ways that matter to this project:

  SELF-EFFORT   The meditations are hand-tagged with a "grace lens": they state
                what God has done, never what the reader must do to trigger it.
                "Try harder to be strong" is structurally perfect and
                theologically off-frame.
  TRANSACTION   The prosperity-gospel shape, which the new Provision mood walks
                straight into: give -> get, sow -> reap, tithe -> open windows.
                Several Provision verses (Malachi 3:10, Luke 6:38, Proverbs
                3:9-10, Deuteronomy 15:10) are the classic proof texts.

Plus two mechanical checks: straight apostrophes (the corpus uses U+2019
throughout) and length outliers (corpus median is 31 characters; a 90-character
meditation will not sit well in 2.3em display type).

Like every scanner here this is a TRIAGE list, not a verdict -- "shall be
blessed" is not automatically transactional. Read the hits.

  python tools/med_scan.py                    # scan merged PROMISES
  python tools/med_scan.py --batches          # scan tools/promises_new/*.json
"""
import sys, os, io, re, json, glob, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epcore as ep

BATCH_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "promises_new")

# Reader-effort as the lever. Deliberately narrow: bare "obey" or "believe" is
# everywhere in scripture and flagging it would drown the signal.
SELF_EFFORT = [
    r"\byou must\b", r"\byou need to\b", r"\byou have to\b",
    r"\bif you only\b", r"\bif you would just\b",
    r"\bstrive\b", r"\btry harder\b", r"\bwork at\b", r"\bearn\b",
    r"\bprove yourself\b", r"\bdeserve\b", r"\bmerit\b",
    r"\bdo your part\b", r"\bmake yourself\b", r"\bqualify\b",
]

# give -> get. The shape, not the vocabulary: "give" alone is fine.
TRANSACTION = [
    r"\bgive\b[^.]{0,30}\b(and|so)\b[^.]{0,30}\b(receive|get|return|back|multipl)",
    r"\bsow\b[^.]{0,30}\breap\b", r"\bseed\b[^.]{0,25}\bharvest\b",
    r"\btithe\b[^.]{0,30}\b(open|bless|pour)", r"\bunlock",
    r"\bwindows of heaven\b[^.]{0,20}\byour\b",
    r"\bthe more you give\b", r"\bhundredfold\b[^.]{0,20}\byour\b",
]

STRAIGHT_APOS = re.compile(r"\w'\w")
LONG = 70

# CALIBRATION -- this is most of the tool's value.
#
# The first run flagged 25 "self-effort" lines and every one was the OPPOSITE:
# "You did not earn this gladness." / "Wisdom is His to give, not yours to
# earn." / "You need not strive; His grace already won." The grace lens is
# expressed by NEGATING the effort verb, so a bare keyword search inverts the
# signal and reports the most on-frame lines in the corpus as defects.
#
# So a hit is suppressed when the effort word sits in a negated or contrastive
# frame. Same discipline as prose_scan.py, whose first quotecap regex produced
# 524 hits that were all correct English.
NEGATED = [
    r"\b(did|do|does|could|need|will|cannot|can|is|was|are)\s*n[o']?t\b",
    r"\bnever\b", r"\bno longer\b", r"\bnothing\b", r"\bwithout\b",
    r"\bnot\s+(yours|your|something|by|to|a)\b",
    r"\bnot\b[^.]{0,20}\b(earn|merit|strive|deserve|prove|work)",
    r"\b(earn|merit|strive|deserve|prove|work\w*)\b[^.]{0,25}\bnot\b",
    r"\brather than\b", r"\binstead of\b", r"\bdon[’']t\b", r"\bfree(ly)?\b",
    r"\bgift\b", r"\bgrace\b", r"\bmercy\b", r"\balready\b",
]


def negated(text):
    """Is the effort word inside a grace-affirming negation or contrast?"""
    return any(re.search(p, text) for p in NEGATED)


def scan(promises, label):
    self_hits, txn_hits, apos, longs = [], [], [], []
    seen = collections.defaultdict(list)

    for p in promises:
        ref = p.get("reference", "?")
        for m in p.get("meditations") or []:
            low = m.lower()
            for pat in SELF_EFFORT:
                if re.search(pat, low) and not negated(low):
                    self_hits.append((ref, m, pat))
                    break
            for pat in TRANSACTION:
                if re.search(pat, low):
                    txn_hits.append((ref, m, pat))
                    break
            if STRAIGHT_APOS.search(m):
                apos.append((ref, m))
            if len(m) > LONG:
                longs.append((ref, len(m), m))
            seen[m.strip().lower()].append(ref)

    cross = {k: v for k, v in seen.items() if len(v) > 1}

    print("=== %s: %d promises, %d meditations ===" % (
        label, len(promises), sum(len(p.get("meditations") or []) for p in promises)))

    def show(name, rows, fmt):
        print("\n%-28s %d" % (name, len(rows)))
        for r in rows[:25]:
            print("   " + fmt(r))
        if len(rows) > 25:
            print("   ... %d more" % (len(rows) - 25))

    show("self-effort language", self_hits, lambda r: "%-22s %s" % (r[0], r[1]))
    show("transactional shape", txn_hits, lambda r: "%-22s %s" % (r[0], r[1]))
    show("straight apostrophe", apos, lambda r: "%-22s %s" % (r[0], r[1]))
    show("over %d chars" % LONG, longs, lambda r: "%-22s (%d) %s" % (r[0], r[1], r[2]))

    print("\n%-28s %d" % ("repeated across promises", len(cross)))
    for k, v in list(cross.items())[:15]:
        print("   %-45s %s" % (k[:45], ", ".join(v[:4])))

    return len(self_hits) + len(txn_hits) + len(apos)


def main():
    ep.utf8_stdout()
    if "--batches" in sys.argv:
        allp = []
        for f in sorted(glob.glob(os.path.join(BATCH_DIR, "*.json"))):
            allp.extend(json.load(io.open(f, encoding="utf-8")))
        scan(allp, "batches")
    else:
        _, P = ep.load(ep.read_lines(), "PROMISES")
        scan(P, "merged PROMISES")


if __name__ == "__main__":
    main()
