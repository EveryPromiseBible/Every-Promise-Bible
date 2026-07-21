# -*- coding: utf-8 -*-
# Luke 4 §0 — five defects.
#
# 1-4. (46, 131, 140, 156) Recitative ὅτι rendered "that" immediately before an
#    opening quotation mark: "It is written, that ‘Not on bread alone...",
#    "it is written that ‘To his angels...", "and that ‘On their hands...",
#    "said to him, that “It has been said:". The quotation mark already does
#    this ὅτι's work. Folded — Greek stays visible, English blank. This is the
#    convention Matthew (the finished book) follows: it has 0 of these.
# 5. (73-76) "and the glory of them," — postposed genitive. -> "and their
#    glory,". αὐτῶν keeps the possessive; the bare article τὴν is folded
#    because "their" now carries it.
CHAPTER = "Luke 4"
SECTION = 0
BLOCKS = [
    (46, 47, [
        (46, ""),                    # ὅτι — recitative, folded
    ]),
    (73, 77, [
        (73, None),                  # καὶ      and
        (76, "their"),               # αὐτῶν
        (74, ""),                    # τὴν — article folded under "their"
        (75, "glory,"),              # δόξαν
    ]),
    (131, 132, [
        (131, ""),                   # ὅτι — recitative, folded
    ]),
    (140, 141, [
        (140, ""),                   # ὅτι — recitative, folded
    ]),
    (156, 157, [
        (156, ""),                   # ὅτι — recitative, folded
    ]),
]
