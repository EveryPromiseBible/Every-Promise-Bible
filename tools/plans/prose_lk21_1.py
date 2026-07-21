# -*- coding: utf-8 -*-
# Luke 21 §1.
#
# BLOCK 1 (155,165) — this one is a MEANING error, not just word order.
#   It read: "for I will give you a mouth and wisdom which will not be able to
#   withstand or contradict all those opposing you."  That says the wisdom is
#   what fails. The Greek is ᾧ οὐ δυνήσονται ἀντιστῆναι ἢ ἀντειπεῖν ἅπαντες οἱ
#   ἀντικείμενοι ὑμῖν — δυνήσονται is 3rd person PLURAL and its subject is
#   ἅπαντες οἱ ἀντικείμενοι ("all those opposing"), which stands at the end in
#   Greek order. The promise is that the OPPONENTS cannot withstand it.
#   Pure reorder restores it:
#     "which all those opposing you will not be able to withstand or contradict."
#   No gloss is re-anchored; only the full stop moves, from ὑμῖν (164) onto
#   ἀντειπεῖν (160), which is now sentence-final.
#
# BLOCK 2 (165,167): "You will be handed over now even by parents…" —
#   postposed δέ. Pure reorder to "Now you will be handed over even by
#   parents…"; only the sentence capital moves with the two glosses.
CHAPTER = "Luke 21"
SECTION = 1
BLOCKS = [
    (155, 165, [
        (155, None),            # ᾗ             which
        (161, None),            # ἅπαντες       all
        (162, None),            # οἱ            those
        (163, None),            # ἀντικείμενοι  opposing
        (164, "you"),           # ὑμῖν
        (156, None),            # οὐ            will not
        (157, None),            # δυνήσονται    be able
        (158, None),            # ἀντιστῆναι    to withstand
        (159, None),            # ἢ             or
        (160, "contradict."),   # ἀντειπεῖν
    ]),
    (165, 167, [
        (166, "Now"),                        # δὲ
        (165, "you will be handed over"),    # παραδοθήσεσθε
    ]),
]
