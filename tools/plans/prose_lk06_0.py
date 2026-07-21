# -*- coding: utf-8 -*-
# Luke 6 §0 — two defects.
#
# 1. (104-108) "were watching closely whether on the Sabbath he heals" — Greek
#    order. -> "whether he heals on the Sabbath". Pure reorder; the comma moves
#    from θεραπεύει onto σαββάτῳ, which now ends the clause.
# 2. (119-120) "he said to the man the one having the withered hand" — the
#    doubled article reads as two separate people. The articular participle
#    τῷ ἔχοντι is an English relative clause: τῷ -> "who", ἔχοντι -> "had".
#    Gloss only, no reorder.
CHAPTER = "Luke 6"
SECTION = 0
BLOCKS = [
    (104, 109, [
        (104, None),                 # εἰ          whether
        (108, "he heals"),           # θεραπεύει
        (105, None),                 # ἐν          on
        (106, None),                 # τῷ          the
        (107, "Sabbath,"),           # σαββάτῳ
    ]),
    (119, 121, [
        (119, "who"),                # τῷ  (was "the one")
        (120, "had"),                # ἔχοντι (was "having")
    ]),
]
