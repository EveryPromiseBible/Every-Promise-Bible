# -*- coding: utf-8 -*-
# Matthew 8 §5: "Now there was far off from them a large herd of pigs feeding."
# read in Greek order (ἦν δὲ μακρὰν ἀπ’ αὐτῶν ἀγέλη χοίρων πολλῶν βοσκομένη);
# reordered to "Now a large herd of pigs was feeding far off from them."
# δὲ, previously folded blank, now carries the sentence-initial "Now"; ἦν, which
# had been glossed "Now there was", is relabelled plainly "was".
CHAPTER = "Matthew 8"
SECTION = 5
BLOCKS = [
    (41, 50, [
        (42, "Now"),        # δὲ         (was folded blank)
        (46, None),         # πολλῶν     — a large
        (47, None),         # ἀγέλη      — herd
        (48, None),         # χοίρων     — of pigs
        (41, "was"),        # ἦν         (was "Now there was")
        (49, "feeding"),    # βοσκομένη  (was "feeding.")
        (43, None),         # μακρὰν     — far off
        (44, None),         # ἀπ’        — from
        (45, "them."),      # αὐτῶν      (was "them")
    ]),
]
