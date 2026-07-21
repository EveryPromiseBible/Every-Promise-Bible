# -*- coding: utf-8 -*-
# Two small stumbles in 2 Peter 2 §2. Both are gloss-only; nothing is reordered,
# so no English word can move onto a different Greek word.
#
# (1) 2:18 read "...they entice by sensual passions of the flesh those who are
#     barely escaping from those who live in error." The instrumental phrase sits
#     between verb and a very long object, so the reader has to back up to find
#     what is being enticed. Setting it off with commas resolves it without
#     moving anything (moving it to the end would let "by sensual passions"
#     re-attach to "escaping", which is worse).
#
# (2) 2:20 read "...and again entangled in them and overcome, the last state has
#     become worse..." — no finite verb, so the clause dangles. ἐμπλακέντες is an
#     aorist passive participle; rendering it as a finite passive ("they are
#     entangled") is the standard move here and lets ἡττῶνται's existing "and
#     overcome" share the auxiliary. The gloss stays on its own Greek word.
CHAPTER = "2 Peter 2"
SECTION = 2
BLOCKS = [
    (119, 123, [
        (119, "they entice,"),      # δελεάζουσιν   — was "they entice"
        (120, None),                # ἐν ἀσελγείαις — by sensual
        (121, None),                # ἐπιθυμίαις    — passions
        (122, "of the flesh,"),     # σαρκὸς        — was "of the flesh"
    ]),
    (157, 158, [
        (157, "they are entangled"),  # ἐμπλακέντες — aor. pass. ptcp; was "entangled"
    ]),
]
