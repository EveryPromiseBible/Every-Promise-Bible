# -*- coding: utf-8 -*-
# Romans 3 §2, two defects. No units are moved; glosses only.
#
# (1) Comma splice. "...a righteousness from God has been revealed, and the Law
#     and the Prophets themselves testify to it, this righteousness of God comes
#     through faith..." — the comma after "it" strands a new main clause.
#     Unit 10 (μαρτυρουμένη ὑπὸ, "themselves testify to it,") ends with a full
#     stop instead, and unit 11 (δικαιοσύνη δὲ, "this righteousness") is
#     capitalised to open the new sentence. Both glosses stay on their own Greek.
#
# (2) Subject-verb disagreement. "Because everyone has sinned and falls short of
#     God's glory, and are justified freely" — "everyone ... are justified" is
#     ungrammatical. πάντες is plural, so gloss it "all" (its plain sense), and
#     put ἥμαρτον / ὑστεροῦνται into the plural they already are: "have sinned",
#     "fall short". δικαιούμενοι keeps "and are justified" and now agrees.
CHAPTER = "Romans 3"
SECTION = 2
BLOCKS = [
    (10, 12, [
        (10, "themselves testify to it."),   # μαρτυρουμένη ὑπὸ
        (11, "This righteousness"),          # δικαιοσύνη δὲ
    ]),
    (26, 30, [
        (26, "all"),            # πάντες
        (27, "have sinned"),    # ἥμαρτον
        (28, None),             # καὶ
        (29, "fall short"),     # ὑστεροῦνται
    ]),
]
