# -*- coding: utf-8 -*-
# Two drifts in Mark 11 §0:
#  (1) 11:2 — adjacent swap the scanner missed: ἐκάθισεν ("sat") was labelled
#      "of men" and ἀνθρώπων ("of men") was labelled "sat.". Reordered so the
#      verb reads "sat." and the genitive noun reads "of men".
#  (2) 11:11 — adjacent swap: the participle οὔσης ("being") was labelled
#      "the hour" and the noun τῆς ὥρας ("the hour") was labelled "being".
CHAPTER = "Mark 11"
SECTION = 0
BLOCKS = [
    (34, 38, [
        (34, None),
        (37, "of men"),
        (36, None),
        (35, "sat."),
    ]),
    (152, 154, [
        (153, "the hour"),
        (152, "being"),
    ]),
]
