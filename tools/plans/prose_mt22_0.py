# -*- coding: utf-8 -*-
# Matthew 22 §0
#  - "Look, my dinner I have prepared;" -> "Look, I have prepared my dinner;"
#    Pure reorder; only the semicolon moves.
#  - "there there will be weeping" stuttered: ἐκεῖ already carries "there",
#    so ἔσται drops its expletive and reads "will be". No unit moved.
CHAPTER = "Matthew 22"
SECTION = 0
BLOCKS = [
    (36, 40, [(36, None), (39, "I have prepared"), (37, None), (38, "dinner;")]),
    (162, 163, [(162, "will be")]),
]
