# -*- coding: utf-8 -*-
# Acts 7 §2 read "At which time was born Moses, and he was beautiful to God" —
# verb-first Greek order left standing. This gives "At which time Moses was born,".
# Pure reorder; only the comma moves from Μωϋσῆς to ἐγεννήθη, which now closes
# the clause.
CHAPTER = "Acts 7"
SECTION = 2
BLOCKS = [
    (47, 52, [
        (47, None),          # ἐν — "At"
        (48, None),          # ᾧ — "which"
        (49, None),          # καιρῷ — "time"
        (51, "Moses"),       # Μωϋσῆς — comma moves off
        (50, "was born,"),   # ἐγεννήθη — now closes the clause
    ]),
]
