# -*- coding: utf-8 -*-
# Matthew 13 §5:
#  (a) "so was fulfilled what was spoken through the prophet: saying," — verb
#      standing before its subject in Greek order. Reordered to
#      "so that what was spoken through the prophet might be fulfilled, saying,".
#  (b) "I will open in parables my mouth" — Greek order. Reordered to
#      "I will open my mouth in parables". Pure reorder.
CHAPTER = "Matthew 13"
SECTION = 5
BLOCKS = [
    (13, 19, [
        (13, "so that"),               # ὅπως
        (15, None),                    # τὸ ῥηθὲν — "what was spoken"
        (16, None),                    # διὰ — "through"
        (17, "the prophet"),           # τοῦ προφήτου
        (14, "might be fulfilled,"),   # πληρωθῇ (aor. pass. subj.)
        (18, None),                    # λέγοντος — "saying,"
    ]),
    (19, 24, [
        (19, None),          # Ἀνοίξω — "‘I will open"
        (22, None),          # μου — "my"
        (23, "mouth"),       # τὸ στόμα
        (20, None),          # ἐν — "in"
        (21, "parables;"),   # παραβολαῖς
    ]),
]
