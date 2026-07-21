# -*- coding: utf-8 -*-
# Luke 9 §2 — two defects.
#
# 1. (58) Recitative ὅτι before an opening quotation mark
#    ("saying that “It is necessary for the Son of Man..."). Folded.
# 2. (148) "when he comes in his glory and of the Father and of the holy
#    angels" — the elliptical genitive series reads as though he comes "of the
#    Father". English needs the ellipsis spelled out; the coordinating καί
#    carries it: "and that of the Father and of the holy angels".
#
# NOTE deliberately left alone: "but himself losing or forfeiting?" is clunky
# but parseable, and every reordering I tried moved δέ's "but" off ἑαυτὸν δὲ
# onto the participle. Not worth the drift.
CHAPTER = "Luke 9"
SECTION = 2
BLOCKS = [
    (57, 59, [
        (57, "saying,"),             # εἰπὼν — supplies the comma the folded
                                     #   ὅτι used to stand between
        (58, ""),                    # ὅτι — recitative, folded
    ]),
    (148, 149, [
        (148, "and that"),           # καὶ — τοῦ (unit 149) already says "of the"
    ]),
]
