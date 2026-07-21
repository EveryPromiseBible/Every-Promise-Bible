# -*- coding: utf-8 -*-
# Luke 22 §4 — three defects.
#
# BLOCK 1 (76,78): read "another certain insisted strongly" — ἄλλος τις with
#   both words glossed as bare determiners, which is not English. Reordered
#   and re-glossed to "someone else insisted strongly":
#     77 τις   "certain" -> "someone"  (τις is the indefinite pronoun; this is
#        its plain English equivalent)
#     76 ἄλλος "another" -> "else"     (ἄλλος means "other"; after "someone",
#        English says that with "else")
#
# BLOCK 2 (123,125): read "how he had said to him that “Before a rooster crows
#   today…" — recitative ὅτι in front of an opening quotation mark. It marks a
#   DIRECT quotation and has no English word of its own; folded, and the comma
#   that introduces the speech moves onto αὐτῷ.
#
# BLOCK 3 (133,134): read "And going out outside, he wept bitterly." —
#   "out outside" is a stutter. ἐξελθὼν is "going (out)" and ἔξω, the very
#   next unit, is "outside"; dropping the redundant "out" from the participle
#   leaves "And going outside, he wept bitterly." Both words still carry their
#   own English and neither is folded.
CHAPTER = "Luke 22"
SECTION = 4
BLOCKS = [
    (76, 78, [
        (77, "someone"),   # τις
        (76, "else"),      # ἄλλος
    ]),
    (123, 125, [
        (123, "to him,"),   # αὐτῷ
        (124, ""),          # ὅτι  recitative — folded
    ]),
    (133, 134, [
        (133, "going"),     # ἐξελθὼν  (ἔξω, next unit, carries "outside")
    ]),
]
