# -*- coding: utf-8 -*-
# Luke 12 §0 — two defects, both Greek order that makes the sentence mean the
# wrong thing rather than merely read stiffly.
#
# 1. (37-45) "whatever in the darkness you have said in the light will be
#    heard" — as written, "in the light" attaches to "you have said", which
#    inverts the saying. -> "whatever you have said in the darkness will be
#    heard in the light". Pure reorder; only the comma moves onto φωτὶ.
# 2. (47-51) "what to the ear you have spoken in the inner rooms" — the
#    prepositional phrase sits before the verb. -> "what you have spoken to the
#    ear in the inner rooms". Pure reorder, no gloss change at all.
CHAPTER = "Luke 12"
SECTION = 0
BLOCKS = [
    (37, 46, [
        (37, None),                  # ὅσα           whatever
        (41, None),                  # εἴπατε        you have said
        (38, None),                  # ἐν            in
        (39, None),                  # τῇ            the
        (40, None),                  # σκοτίᾳ        darkness
        (45, "will be heard"),       # ἀκουσθήσεται
        (42, None),                  # ἐν            in
        (43, None),                  # τῷ            the
        (44, "light,"),              # φωτὶ
    ]),
    (47, 52, [
        (47, None),                  # ὃ             what
        (51, None),                  # ἐλαλήσατε     you have spoken
        (48, None),                  # πρὸς          to
        (49, None),                  # τὸ            the
        (50, None),                  # οὖς           ear
    ]),
]
