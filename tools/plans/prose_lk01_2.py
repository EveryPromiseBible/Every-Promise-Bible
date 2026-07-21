# -*- coding: utf-8 -*-
# Luke 1 §2 — three defects, one of them real gloss drift.
#
# 1. "she was pondering what kind greeting this might be" — ungrammatical.
#    ποταπὸς is "what sort of"; regloss 46 only. No reorder.
# 2. "and Son of the Most High he will be called;" is Greek order.
#    Front κληθήσεται. The semicolon rides to the new last unit (Ὑψίστου).
# 3. *** GLOSS DRIFT *** units 130/131 were crossed:
#       τὸ γεννώμενον  ("the one being born")  was labelled "the holy one"
#       ἅγιον          ("holy")                was labelled "to be born"
#    Click γεννώμενον on the site and the popup said "the holy one".
#    Repaired by putting each gloss back on its own word and reordering to the
#    predicate reading (cf. ESV "the child to be born will be called holy—
#    the Son of God"), which reads naturally with the glosses correct:
#    "therefore also the one to be born will be called holy, the Son of God."
CHAPTER = "Luke 1"
SECTION = 2
BLOCKS = [
    (46, 47, [
        (46, "what kind of"),          # ποταπὸς
    ]),
    (79, 82, [
        (81, "he will be called"),     # κληθήσεται
        (79, None),                    # υἱὸς      Son
        (80, "of the Most High;"),     # Ὑψίστου — takes the semicolon
    ]),
    (130, 135, [
        (130, "the one to be born"),   # τὸ γεννώμενον  (was "the holy one")
        (132, None),                   # κληθήσεται     will be called
        (131, "holy,"),                # ἅγιον          (was "to be born")
        (133, "the Son"),              # υἱὸς
        (134, None),                   # θεοῦ           of God.
    ]),
]
