# -*- coding: utf-8 -*-
# Luke 22 §1 fix — clear the standalone em-dash placeholder at idx 6
# (Greek article τὸ). Attach a comma to "them" and fold the placeholder:
# "a rivalry among them, which of them seemed to be greatest."
CHAPTER = "Luke 22"
SECTION = 1
BLOCKS = [
    (5, 7, [(5,"them,"),(6,"")]),
]
