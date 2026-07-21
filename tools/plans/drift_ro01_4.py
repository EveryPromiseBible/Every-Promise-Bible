# -*- coding: utf-8 -*-
# Romans 1:30 -- exchanged labels, found by tools/swap_scan.py.
# The vice list reads "God-haters, arrogant, boastful, and proud," which is
# correct English, so no prose pass could see the problem. Underneath:
#     95 ὑπερηφάνους  labelled "boastful,"    -- G5244 is "proud"
#     96 ἀλαζόνας     labelled "and proud,"   -- G213 is "boaster"
# The two are wearing each other's labels. (ESV: "insolent, haughty, boastful",
# i.e. ὑπερήφανος = haughty/proud, ἀλαζών = boastful.)
#
# Fixed as a pure REORDER, so the visible sentence is byte-identical and only
# the anchoring changes -- the same shape as the John 4:12 repair:
#     ἀλαζόνας    now carries "boastful,"   (its own sense)
#     ὑπερηφάνους now carries "and proud,"  (its own sense)
CHAPTER = "Romans 1"
SECTION = 4
BLOCKS = [
    (95, 97, [
        (96, "boastful,"),    # ἀλαζόνας   G213 boaster
        (95, "and proud,"),   # ὑπερηφάνους G5244 proud
    ]),
]
