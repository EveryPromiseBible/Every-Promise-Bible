# -*- coding: utf-8 -*-
# Acts 17:6-8, two small stumbles in one section.
# (a) "...officials, shouting “These men..." -- speech verb has no comma before
#     the quotation mark. 96 βοῶντες ὅτι "shouting" -> "shouting," (ὅτι stays
#     folded into the quote-opening, unchanged in force).
# (b) "And they stirred up the crowd and the city officials hearing this." --
#     the participle ἀκούοντας dangles off "officials" and reads as though the
#     officials were doing the hearing mid-clause. Rendered as the relative it
#     is: 122 "hearing" -> "who heard", 123 ταῦτα "this." unchanged in sense but
#     kept as "these things." for the relative clause to close cleanly.
CHAPTER = "Acts 17"
SECTION = 0
BLOCKS = [
    (96, 97, [
        (96, "shouting,"),          # βοῶντες ὅτι
    ]),
    (122, 124, [
        (122, "who heard"),         # ἀκούοντας
        (123, "these things."),     # ταῦτα
    ]),
]
