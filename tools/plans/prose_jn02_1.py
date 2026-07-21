# -*- coding: utf-8 -*-
# John 2:20 read "and you in three days will raise it?" — Greek order standing in
# English. This gives "and you will raise it in three days?", which matches the
# natural English of the parallel clause a line earlier ("in three days I will
# raise it").
# Only two glosses change, both punctuation-only:
#   131 ἡμέραις "days" now carries the "?" and the closing quote (it ends the sentence)
#   133 αὐτόν  "it" loses the "?" and closing quote (it is no longer last)
# Every English word stays on the same Greek word it was already anchored to.
CHAPTER = "John 2"
SECTION = 1
BLOCKS = [
    (127, 134, [
        (127, None),        # καὶ    — and
        (128, None),        # σὺ     — you
        (132, None),        # ἐγερεῖς— will raise
        (133, "it"),        # αὐτόν  — it
        (129, None),        # ἐν     — in
        (130, None),        # τρισὶν — three
        (131, "days?”"),    # ἡμέραις— days
    ]),
]
