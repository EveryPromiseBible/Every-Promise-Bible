# -*- coding: utf-8 -*-
# Matthew 19 §1: "Let the little children and do not hinder them come to me" —
# the infinitive ἐλθεῖν was stranded at the end in Greek order, splitting
# "Let … come to me". Reordered to "Let the little children come to me, and do
# not hinder them". Pure reorder.
CHAPTER = "Matthew 19"
SECTION = 1
BLOCKS = [
    (16, 25, [
        (16, None),        # Ἄφετε — "“Let"
        (17, None),        # τὰ παιδία — "the little children"
        (22, None),        # ἐλθεῖν — "come"
        (23, None),        # πρός — "to"
        (24, None),        # με — "me,"
        (18, None),        # καὶ — "and"
        (19, None),        # μὴ — "do not"
        (20, None),        # κωλύετε — "hinder"
        (21, "them,"),     # αὐτὰ
    ]),
]
