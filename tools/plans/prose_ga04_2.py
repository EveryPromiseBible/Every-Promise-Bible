# -*- coding: utf-8 -*-
# Galatians 4:9 renders "...you have come to know God— or rather to be known by
# God— how can you turn back again..." Both em dashes are glued to the preceding
# word with no space before and a space after, which reads as a typo. Galatians'
# own convention elsewhere is a spaced em dash ("Paul, an apostle — not from men").
#
# Pure gloss rewrite, no reordering. Only a space is inserted; the dash stays on the
# same unit it was already on, so the anchoring is untouched:
#   14 θεόν     "God—"     -> "God —"     (still glosses θεόν, "God")
#   17 ὑπὸ θεοῦ "by God—"  -> "by God —"  (still glosses ὑπὸ θεοῦ, "by God")
CHAPTER = "Galatians 4"
SECTION = 2
BLOCKS = [
    (14, 15, [
        (14, "God —"),      # θεόν
    ]),
    (17, 18, [
        (17, "by God —"),   # ὑπὸ θεοῦ
    ]),
]
