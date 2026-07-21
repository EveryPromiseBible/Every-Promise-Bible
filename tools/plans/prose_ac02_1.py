# -*- coding: utf-8 -*-
# Acts 2 §1 (Joel quotation) read "…before the day of the Lord comes— the great
# and glorious." The attributive phrase τὴν μεγάλην καὶ ἐπιφανῆ was left trailing
# in Greek order behind its noun. This gives "…before the great and glorious day
# of the Lord comes."
#
# Anchoring: τὴν is the article and now carries "the" (it previously carried a
# bare "the" too); ἡμέραν drops the article it was borrowing and reads "day";
# ἐλθεῖν takes the sentence-final full stop that ἐπιφανῆ used to hold, and the
# em-dash that marked the trailing apposition is no longer needed.
CHAPTER = "Acts 2"
SECTION = 1
BLOCKS = [
    (138, 146, [
        (138, None),       # πρὶν ἢ — "before"
        (142, None),       # τὴν — "the"
        (143, None),       # μεγάλην — "great"
        (144, None),       # καὶ — "and"
        (145, "glorious"), # ἐπιφανῆ — full stop moves off
        (139, "day"),      # ἡμέραν — article now sits on τὴν
        (140, None),       # κυρίου — "of the Lord"
        (141, "comes."),   # ἐλθεῖν — now ends the sentence
    ]),
]
