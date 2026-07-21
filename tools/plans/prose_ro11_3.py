# -*- coding: utf-8 -*-
# Romans 11 §3 opened with a sentence that never resolves:
#   "Now if some of the branches have been broken off, and you, a wild olive
#    shoot, have been grafted in among them and now share in the nourishing sap
#    of the olive root, and now don't boast over those branches."
# Two problems, one cause. ἐγένου ("you have become") sits at the far end of its
# clause in Greek order and had been reduced to a bare connective "and now" —
# a drifted gloss, since ἐγένου is a verb, not a conjunction. That left the
# apodosis ("don't boast") hanging off a second spurious "and now", so the whole
# conditional reads as a fragment.
#
# Fix, within [8,15): ἐγένου moves up to where English wants the verb and gets
# its own honest gloss "have become"; συγκοινωνὸς ("fellow-partaker") becomes
# the noun it is, "a sharer in", instead of carrying the verb force it never had.
# Units 10-13 (τῆς πιότητος / τῆς ῥίζης / τῆς ἐλαίας / filler "root,") keep both
# their order and their glosses untouched. Nothing is added or dropped; the
# comma before the imperative survives on the filler as before.
#
# Result: "...have been grafted in among them and have become a sharer in the
# nourishing sap of the olive root, don't boast over those branches."
CHAPTER = "Romans 11"
SECTION = 3
BLOCKS = [
    (8, 15, [
        (8, None),                # καὶ — "and"
        (14, "have become"),      # ἐγένου
        (9, "a sharer in"),       # συγκοινωνὸς
        (10, None),               # τῆς πιότητος — "the nourishing sap"
        (11, None),               # τῆς ῥίζης — "of the"
        (12, None),               # τῆς ἐλαίας — "olive"
        (13, None),               # filler — "root,"
    ]),
]
