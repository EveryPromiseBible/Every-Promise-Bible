# -*- coding: utf-8 -*-
# John 14 §0 has offset quotation marks. The section opens mid-air with
# "Do not let your heart be troubled." and no opening quote, yet four sentences
# later closes one: "…you know the way.”" At the other end, Jesus' reply to
# Philip opens with “ and the section simply stops — "…I will do it." with no
# close. (John 13 §3 closes its own quotation, and John 14 §1 and §2 each open
# and close their own, so this section is the odd one out.)
# Two punctuation-only gloss edits; no unit moves and no word changes:
#   0   Μὴ      "Do not let"   -> "“Do not let"    (opens the speech)
#   249 ποιήσω  "will do it."  -> "will do it.”"   (closes it)
CHAPTER = "John 14"
SECTION = 0
BLOCKS = [
    (0, 1, [
        (0, "“Do not let"),        # Μὴ
    ]),
    (249, 250, [
        (249, "will do it.”"),     # ποιήσω
    ]),
]
