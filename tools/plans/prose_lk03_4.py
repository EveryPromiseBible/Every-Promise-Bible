# -*- coding: utf-8 -*-
# Luke 3 §4 (the genealogy) — two defects.
#
# 1. *** GLOSS DRIFT *** (7-9). The glosses "years / old, / being a son—" were
#    spread one word to the left of the Greek they belong to:
#       ἐτῶν  ("years")      was labelled "years"      -> should carry "old" too
#       ὢν    ("being")      was labelled "old,"
#       υἱός  ("a son")      was labelled "being a son—"
#    Click ὢν and the popup said "old,". Repaired in place — the prose is
#    identical, each gloss now sits on its own word. No reorder.
# 2. (88) The list ended "of Adam, —of God." — a stray em dash after a comma.
#    Dropped so the final link reads "of Adam, of God." like every other link.
CHAPTER = "Luke 3"
SECTION = 4
BLOCKS = [
    (7, 10, [
        (7, "years old,"),           # ἐτῶν
        (8, "being"),                # ὢν    (was "old,")
        (9, "a son—"),               # υἱός  (was "being a son—")
    ]),
    (88, 89, [
        (88, "of God."),             # τοῦ θεοῦ
    ]),
]
