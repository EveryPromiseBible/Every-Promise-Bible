# -*- coding: utf-8 -*-
# Acts 9 §3 — two gloss-only repairs, no reorder.
#
# 1) "; whom, arriving, they brought up into the upper room" — the bare
#    participle reads as though the subject of "arriving" were "they". The aorist
#    participle παραγενόμενον agrees with ὅν (Peter), so spelling it out as
#    "when he had arrived," removes the misreading without moving anything.
#
# 2) "But Peter, putting everyone outside, and bowing his knees, he prayed;" —
#    "Peter" is already the stated subject, so the resumptive "he" breaks the
#    sentence. προσηύξατο -> "prayed;".
CHAPTER = "Acts 9"
SECTION = 3
BLOCKS = [
    (129, 130, [
        (129, "when he had arrived,"),  # παραγενόμενον
    ]),
    (163, 164, [
        (163, "prayed;"),               # προσηύξατο
    ]),
]
