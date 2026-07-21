# -*- coding: utf-8 -*-
# Two Greek-order sentences in John 11 §4.
#
# BLOCK 1 — John 11:52 read "but so that also the scattered children of God he
#   might gather together into one." The object sits in front of its verb, so the
#   reader reaches "he might gather" with the sentence already spent. Now:
#   "but so that he might gather together also the scattered children of God into
#   one." PURE reorder — no gloss changes at all, and ἕν still ends the sentence
#   so it keeps its full stop.
#
# BLOCK 2 — John 11:54 read "to Ephraim, called a town" — which says the town is
#   named "a town". λεγομένην πόλιν modifies Ἐφραὶμ: "to a town called Ephraim".
#   One punctuation-only gloss edit: 173 πόλιν "a town," -> "a town" (the comma
#   moves to Ἐφραὶμ, which already carries one and now ends the phrase).
CHAPTER = "John 11"
SECTION = 4
BLOCKS = [
    (132, 143, [
        (132, None),      # ἵνα             — so that
        (140, None),      # συναγάγῃ        — he might gather together
        (133, None),      # καὶ             — also
        (134, None),      # τὰ              — the
        (135, None),      # διεσκορπισμένα  — scattered
        (136, None),      # τέκνα           — children
        (137, None),      # τοῦ             — of
        (138, None),      # θεοῦ            — God
        (139, None),      # τὰ              — ·(folded)
        (141, None),      # εἰς             — into
        (142, None),      # ἕν              — one.
    ]),
    (170, 174, [
        (170, None),        # εἰς        — to
        (173, "a town"),    # πόλιν
        (172, None),        # λεγομένην  — called
        (171, None),        # Ἐφραὶμ     — Ephraim,
    ]),
]
