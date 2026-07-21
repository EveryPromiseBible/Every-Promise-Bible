# -*- coding: utf-8 -*-
# Luke 20 §2 — two defects.
#
# BLOCK 1 (29,33): read "we know that rightly you speak and teach," — adverb
#   fronted in Greek order (ὀρθῶς λέγεις καὶ διδάσκεις). Pure reorder to
#   "we know that you speak and teach rightly,". Only the comma moves, from
#   διδάσκεις onto ὀρθῶς.
#
# BLOCK 2 (99,102): read "and marveling at the answer of his, they fell
#   silent." — postposed genitive. Fixed to "and marveling at his answer,":
#     99  τῇ     "the"      -> ""     folded. English "his" already carries
#         the definiteness, so the article has no separate English word — the
#         same fold this project used to clear the postposed genitives in
#         Romans.
#     101 αὐτοῦ  "of his"   -> "his"
#     100 ἀποκρίσει "answer" -> "answer,"  (takes the comma from αὐτοῦ)
CHAPTER = "Luke 20"
SECTION = 2
BLOCKS = [
    (29, 33, [
        (30, None),        # λέγεις      you speak
        (31, None),        # καὶ         and
        (32, "teach"),     # διδάσκεις
        (29, "rightly,"),  # ὀρθῶς
    ]),
    (99, 102, [
        (99, ""),          # τῇ          article — folded
        (101, "his"),      # αὐτοῦ
        (100, "answer,"),  # ἀποκρίσει
    ]),
]
