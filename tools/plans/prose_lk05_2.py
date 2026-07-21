# -*- coding: utf-8 -*-
# Luke 5 §2 — two folds, no reordering.
#
# 1. (5) "And it happened on one of the days, and he was teaching, and there
#    were sitting Pharisees..." — the Semitic apodosis καί after ἐγένετο leaves
#    the opening clause dangling with no main verb. Folded.
#    NOTE: "there were sitting Pharisees" is deliberately left alone — it is a
#    correct English existential inversion, and over-triggering on it broke
#    this very section once before (see PROJECT.md §11).
# 2. (179) Recitative ὅτι before an opening quotation mark
#    ("saying, that “We have seen incredible things today!”"). Folded.
CHAPTER = "Luke 5"
SECTION = 2
BLOCKS = [
    (5, 6, [
        (5, ""),                     # καὶ — apodosis, folded
    ]),
    (179, 180, [
        (179, ""),                   # ὅτι — recitative, folded
    ]),
]
