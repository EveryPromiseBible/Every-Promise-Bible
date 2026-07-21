# -*- coding: utf-8 -*-
# Luke 11 §3 — one defect.
# "These things now it was necessary to do, and those things not to neglect."
# The fronted object leaves the sentence opening with a dangling "These things
# now". Reordered to "Now it was necessary to do these things, and those things
# not to neglect." The trailing clause is left elliptical on purpose — it now
# reads as a deliberate parallel rather than as stranded Greek order.
# Pure reorder; only the capital and comma move.
CHAPTER = "Luke 11"
SECTION = 3
BLOCKS = [
    (91, 95, [
        (92, "Now"),                 # δὲ
        (93, None),                  # ἔδει     it was necessary
        (94, "to do"),               # ποιῆσαι — comma moves to ταῦτα below
        (91, "these things,"),       # ταῦτα
    ]),
]
