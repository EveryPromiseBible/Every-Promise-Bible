# -*- coding: utf-8 -*-
# Galatians 4:19-20 renders "...until Christ is formed in you— I wish I could be
# present..." Same defect as 4 §2: the em dash is glued to the preceding word with
# no space before it and a space after, which reads as a typo against Galatians'
# own spaced-em-dash convention.
#
# Pure gloss rewrite, no reordering. Only a space is inserted; the dash stays on the
# unit it was already on:
#   26 ἐν ὑμῖν "in you—" -> "in you —"   (still glosses ἐν ὑμῖν, "in you")
CHAPTER = "Galatians 4"
SECTION = 4
BLOCKS = [
    (26, 27, [
        (26, "in you —"),   # ἐν ὑμῖν
    ]),
]
