# -*- coding: utf-8 -*-
# Acts 7 §5 — two Greek-order clauses.
#
# 1) "of whom now you betrayers and murderers have become;" -> "of whom you now
#    have become betrayers and murderers;". Pure reorder; only the semicolon
#    moves from ἐγένεσθε to φονεῖς, which now closes the clause.
#
# 2) "And this having said, he fell asleep." -> "And having said this, he fell
#    asleep." Pure reorder; only the comma moves from εἰπὼν to τοῦτο.
CHAPTER = "Acts 7"
SECTION = 5
BLOCKS = [
    (37, 44, [
        (37, None),           # οὗ — "of whom"
        (39, None),           # ὑμεῖς — "you"
        (38, None),           # νῦν — "now"
        (43, "have become"),  # ἐγένεσθε — semicolon moves off
        (40, None),           # προδόται — "betrayers"
        (41, None),           # καὶ — "and"
        (42, "murderers;"),   # φονεῖς — now closes the clause
    ]),
    (162, 165, [
        (162, None),          # καὶ — "And"
        (164, "having said"), # εἰπὼν — comma moves off
        (163, "this,"),       # τοῦτο — now closes the participial phrase
    ]),
]
