# -*- coding: utf-8 -*-
# Luke 16 §2 — two Greek-order clauses.
#
# BLOCK 1 (10,14): "celebrating every day splendidly." — the manner adverb
#   stranded after the time phrase (Greek καθ’ ἡμέραν λαμπρῶς). Pure reorder
#   to "celebrating splendidly every day."  The full stop moves from λαμπρῶς
#   onto the new final word ἡμέραν; no gloss is re-anchored.
#
# BLOCK 2 (160,165): "nor from there to us may they cross.’" — verb stranded
#   at the end behind both prepositional phrases. Pure reorder to
#   "nor may they cross from there to us.’"  The full stop AND the closing
#   single quotation mark travel together from διαπερῶσιν onto the new final
#   unit ἡμᾶς, so Abraham's speech still closes.
CHAPTER = "Luke 16"
SECTION = 2
BLOCKS = [
    (10, 14, [
        (10, None),            # εὐφραινόμενος  celebrating
        (13, "splendidly"),    # λαμπρῶς
        (11, None),            # καθ’           every
        (12, "day."),          # ἡμέραν
    ]),
    (160, 165, [
        (160, None),                 # μηδὲ         nor
        (164, "may they cross"),     # διαπερῶσιν
        (161, None),                 # ἐκεῖθεν      from there
        (162, None),                 # πρὸς         to
        (163, "us.’"),               # ἡμᾶς
    ]),
]
