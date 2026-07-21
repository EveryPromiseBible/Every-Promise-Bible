# -*- coding: utf-8 -*-
# Acts 21:11 read "'The man whose this belt is the Jews in Jerusalem will tie up
# like this...'" -- "whose this belt is" is not English, and with no punctuation
# after it the reader runs "is the Jews" together and has to restart.
# The demonstrative αὕτη is folded inside unit 70 (ἡ ζώνη αὕτη), so "belt" and
# "this" cannot be reordered past each other; recast the relative instead:
#   69 οὗ    "whose" -> "to whom"   (possessive genitive relative -- same force)
#   71 ἐστιν "is"    -> "belongs —" (ἐστίν with a possessive genitive is exactly
#                                    "belongs to"; the dash closes the fronted
#                                    object before the subject arrives)
# 70 ἡ ζώνη αὕτη keeps "this belt" unchanged.
CHAPTER = "Acts 21"
SECTION = 1
BLOCKS = [
    (69, 72, [
        (69, "to whom"),      # οὗ
        (70, None),           # ἡ ζώνη αὕτη  "this belt"
        (71, "belongs —"),    # ἐστιν
    ]),
]
