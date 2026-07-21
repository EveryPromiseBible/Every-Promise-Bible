# -*- coding: utf-8 -*-
# Matthew 26 §2:
#  - "Then went one of the twelve, ... to the chief priests" -> "Then one of
#    the twelve, ... went to the chief priests".  Pure reorder.
#  - "and I to you will deliver him?" -> "and I will deliver him to you?"
#    Pure reorder; only the "?" travels.
CHAPTER = "Matthew 26"
SECTION = 2
BLOCKS = [
    (0, 7, [(0, None), (2, None), (3, None), (4, None), (5, None), (6, None),
            (1, None)]),
    (14, 18, [(14, None), (16, None), (17, "him"), (15, "to you?”")]),
]
