# -*- coding: utf-8 -*-
# Matthew 15 §4:
#  (a) "And to send them away hungry I do not want," — Greek order. Reordered to
#      "And I do not want to send them away hungry,". Pure reorder.
#  (b) "they may collapse on on the way" — "on" was duplicated across ἐν and
#      τῇ ὁδῷ. Reglossed τῇ ὁδῷ as "the way.”".
CHAPTER = "Matthew 15"
SECTION = 4
BLOCKS = [
    (19, 26, [
        (19, None),        # καὶ — "And"
        (24, None),        # οὐ — "I do not"
        (25, "want"),      # θέλω
        (20, None),        # ἀπολῦσαι — "to send"
        (21, None),        # αὐτοὺς — "them"
        (22, None),        # (supplied filler) — "away"
        (23, "hungry,"),   # νήστεις
    ]),
    (29, 30, [
        (29, "the way.”"),  # τῇ ὁδῷ
    ]),
]
