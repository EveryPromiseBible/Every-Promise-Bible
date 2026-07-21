# -*- coding: utf-8 -*-
# Acts 9 §2 read "Is not this the man who ravaged in Jerusalem those calling on
# this name?" — the locative sat between the verb and its object, in Greek order.
# This gives "…who ravaged those calling on this name in Jerusalem?"
# Pure reorder; only the question mark moves from ὄνομα to Ἰερουσαλήμ, which now
# closes the question.
CHAPTER = "Acts 9"
SECTION = 2
BLOCKS = [
    (26, 34, [
        (26, None),           # πορθήσας — "who ravaged"
        (29, None),           # τοὺς — "those"
        (30, None),           # ἐπικαλουμένους — "calling on"
        (31, None),           # τὸ — folded
        (32, None),           # τοῦτο — "this"
        (33, "name"),         # ὄνομα — question mark moves off
        (27, None),           # ἐν — "in"
        (28, "Jerusalem?"),   # Ἰερουσαλὴμ — now closes the question
    ]),
]
