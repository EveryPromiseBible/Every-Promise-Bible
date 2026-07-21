# -*- coding: utf-8 -*-
# 1 Corinthians 10:8 read "...and fell in one day twenty three thousand."
# That is Greek order (καὶ ἔπεσαν μιᾷ ἡμέρᾳ εἴκοσι τρεῖς χιλιάδες) with the
# subject stranded at the very end, so the reader meets a verb with no subject
# and has to re-read. Pure reorder — subject before verb — plus moving the full
# stop to the new last unit:
#   41 χιλιάδες "thousand." -> "thousand"
#   38 ἡμέρᾳ    "day"       -> "day."
# Gives: "...as some of them did, and twenty three thousand fell in one day."
CHAPTER = "1 Corinthians 10"
SECTION = 1
BLOCKS = [
    (35, 42, [
        (35, None),          # καὶ — "and"
        (39, None),          # εἴκοσι — "twenty"
        (40, None),          # τρεῖς — "three"
        (41, "thousand"),    # χιλιάδες
        (36, None),          # ἔπεσαν — "fell"
        (37, None),          # μιᾷ — "in one"
        (38, "day."),        # ἡμέρᾳ
    ]),
]
