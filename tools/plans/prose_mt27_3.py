# -*- coding: utf-8 -*-
# Matthew 27 §3:
#  - "wine with gall mixed;" -> "wine mixed with gall;"  Pure reorder.
#  - "Then there were crucified with him two rebels," -> "Then two rebels were
#    crucified with him,".  Reorder; σταυροῦνται drops the expletive "there".
#  - "'Of God I am the Son.'" -> "'I am the Son of God.'"  Pure reorder; the
#    same three glosses already read this way at "the Son of God" above.
#  - "And the same also the rebels ... reviled him." -> "And in the same way
#    also the rebels ... reviled him."  Gloss only on τὸ δ’ αὐτὸ.
CHAPTER = "Matthew 27"
SECTION = 3
BLOCKS = [
    (26, 30, [(26, None), (29, "mixed"), (27, None), (28, "gall;")]),
    (60, 66, [(60, None), (64, None), (65, "rebels"), (61, "were crucified"),
              (62, None), (63, "him,")]),
    (134, 137, [(135, "‘I am"), (136, "the Son"), (134, "of God.’”")]),
    (137, 138, [(137, "And in the same way")]),
]
