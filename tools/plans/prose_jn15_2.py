# -*- coding: utf-8 -*-
# John 15:27 read "because from the beginning with me you are." — Greek order
# left standing, and it ends the chapter on a sentence the reader has to unpick
# backwards. Now: "because you are with me from the beginning."
# Two gloss edits, both punctuation only:
#   182 ἐστε   "you are.”"     -> "you are"        (no longer final)
#   179 ἀρχῆς  "the beginning" -> "the beginning.”" (now ends the speech, so it
#                                                    takes the stop and the close-quote)
CHAPTER = "John 15"
SECTION = 2
BLOCKS = [
    (177, 183, [
        (177, None),                # ὅτι    — because
        (182, "you are"),           # ἐστε
        (180, None),                # μετ’   — with
        (181, None),                # ἐμοῦ   — me
        (178, None),                # ἀπ’    — from
        (179, "the beginning.”"),   # ἀρχῆς
    ]),
]
