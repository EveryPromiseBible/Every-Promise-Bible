# -*- coding: utf-8 -*-
# Luke 4 §1 — three defects.
#
# 1. (48-52) "And the scroll was handed to him, of the prophet Isaiah;" — the
#    genitive is stranded after the verb. -> "And the scroll of the prophet
#    Isaiah was handed to him;". Pure reorder; only the punctuation moves
#    (the semicolon from Ἠσαΐου onto αὐτῷ).
# 2. (82) "to send out the oppressed in release;" — "in release" is opaque
#    English. ἀφέσει is the same noun already rendered "release" at unit 74,
#    so here it takes its other standard sense, "freedom". Gloss only.
# 3. (106) Recitative ὅτι before an opening quotation mark
#    ("began to say to them, that “Today..."). Folded.
CHAPTER = "Luke 4"
SECTION = 1
BLOCKS = [
    (48, 53, [
        (48, None),                  # βιβλίον       the scroll
        (51, None),                  # τοῦ προφήτου  of the prophet
        (52, "Isaiah"),              # Ἠσαΐου
        (49, None),                  # ἐπεδόθη       was handed
        (50, "to him;"),             # αὐτῷ
    ]),
    (82, 83, [
        (82, "freedom;"),            # ἀφέσει
    ]),
    (106, 107, [
        (106, ""),                   # ὅτι — recitative, folded
    ]),
]
