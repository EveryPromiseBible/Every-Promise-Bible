# -*- coding: utf-8 -*-
# Acts 4 §1 read:
#   "For that a notable sign has happened through them to all those living in
#    Jerusalem is plain, and we cannot deny it."
# φανερόν ("is plain") was pushed to the end in Greek order, which stranded its
# dative πᾶσιν τοῖς κατοικοῦσιν Ἰερουσαλήμ next to "has happened" — so the
# English read as though the sign happened *to* everyone in Jerusalem, and the
# predicate arrived only after eleven words. This gives:
#   "For that a notable sign has happened through them is plain to all those
#    living in Jerusalem, and we cannot deny it."
#
# This is a pure reorder: no gloss is rewritten. Only the comma moves from
# φανερόν to Ἰερουσαλήμ, which now closes the clause.
CHAPTER = "Acts 4"
SECTION = 1
BLOCKS = [
    (52, 63, [
        (52, None),          # ὅτι μὲν γὰρ — "For that"
        (53, None),          # γνωστὸν — "a notable"
        (54, None),          # σημεῖον — "sign"
        (55, None),          # γέγονεν — "has happened"
        (56, None),          # δι’ — "through"
        (57, None),          # αὐτῶν — "them"
        (62, "is plain"),    # φανερόν — comma moves off
        (58, None),          # πᾶσιν — "to all"
        (59, None),          # τοῖς — "those"
        (60, None),          # κατοικοῦσιν — "living in"
        (61, "Jerusalem,"),  # Ἰερουσαλὴμ — now closes the clause
    ]),
]
