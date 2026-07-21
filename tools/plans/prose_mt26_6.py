# -*- coding: utf-8 -*-
# Matthew 26 §6:
#  - "And the betrayer him gave them a signal" -> "And the one betraying him
#    gave them a signal".  Gloss only; ὁ παραδιδοὺς is already read "the one
#    betraying" twice earlier in this chapter, and αὐτὸν is its object.
#  - "How then would be fulfilled the Scriptures" -> "How then would the
#    Scriptures be fulfilled".  Pure reorder.
#  - "But this all has taken place so that might be fulfilled the writings of
#    the prophets." -> "But all this has taken place so that the writings of
#    the prophets might be fulfilled."  Pure reorder; the period travels.
#  - "Then the disciples all deserting him fled." -> "Then all the disciples,
#    deserting him, fled."  Pure reorder; commas added.
CHAPTER = "Matthew 26"
SECTION = 6
BLOCKS = [
    (23, 24, [(23, "the one betraying")]),
    (109, 113, [(109, None), (110, None), (112, None), (111, None)]),
    (143, 145, [(144, None), (143, None)]),
    (146, 150, [(146, None), (148, None), (149, "of the prophets"),
                (147, "might be fulfilled.”")]),
    (150, 156, [(150, None), (152, None), (151, "the disciples,"), (153, None),
                (154, "him,"), (155, None)]),
]
