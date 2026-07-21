# -*- coding: utf-8 -*-
# Galatians 3:7 renders "those who are of faith —these are the sons of Abraham."
# Same defect as 3 §0: the em dash is carried as a prefix on unit 15 (οὗτοι), so the
# joiner emits " —these" — space before the dash, none after. Reads as a typo.
#
# Pure gloss rewrite, no reordering. The dash moves to the end of πίστεως and οὗτοι
# keeps its own honest gloss "these":
#   14 πίστεως "faith"   -> "faith —"   (still glosses πίστεως, "faith")
#   15 οὗτοι   "—these"  -> "these"     (still glosses οὗτοι, "these")
CHAPTER = "Galatians 3"
SECTION = 1
BLOCKS = [
    (14, 16, [
        (14, "faith —"),   # πίστεως
        (15, "these"),     # οὗτοι
    ]),
]
