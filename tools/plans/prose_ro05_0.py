# -*- coding: utf-8 -*-
# Romans 5 §0 ends mid-punctuation: "...through the Holy Spirit he's given us,"
# The trailing comma dangles — §1 opens with a fresh capitalised sentence
# ("Because at just the right time..."), so nothing continues it. Reads as a typo.
# Unit 61 (ἡμῖν, "us,") becomes "us." Nothing moves; punctuation only.
CHAPTER = "Romans 5"
SECTION = 0
BLOCKS = [
    (60, 62, [
        (60, None),   # τοῦ δοθέντος — "he's given"
        (61, "us."),  # ἡμῖν
    ]),
]
