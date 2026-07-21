# -*- coding: utf-8 -*-
# 1 Corinthians 1:19 read "...and the understanding of the understanding I will
# set aside." The stutter is a gloss collision: σύνεσιν (the faculty) and
# συνετῶν (the people who have it) were both glossed "understanding".
# Fix is gloss-only, no reorder:
#   19 σύνεσιν  "the understanding" -> "the discernment"  (σύνεσις = discernment,
#      insight — the noun for the faculty; honest and standard)
#   20 συνετῶν  "of the understanding" -> "of the discerning" (συνετός =
#      intelligent/discerning, substantival plural = the discerning ones)
# Fronted object ("the discernment ... I will set aside") is kept — it is the
# Isaiah 29:14 parallelism and reads normally in English.
CHAPTER = "1 Corinthians 1"
SECTION = 3
BLOCKS = [
    (19, 21, [
        (19, "the discernment"),    # τὴν σύνεσιν
        (20, "of the discerning"),  # τῶν συνετῶν
    ]),
]
