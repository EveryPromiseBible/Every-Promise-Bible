# -*- coding: utf-8 -*-
# Matthew 27 §2:
#  - "gathered around him the whole company." -> "gathered the whole company
#    around him."  Pure reorder; the period travels.
#  - "and struck on his head." had no object: ἔτυπτον now reads "struck him".
#  - "they took off him the robe and put on him his clothes" -> "they stripped
#    him of the robe and dressed him in his clothes".  Gloss only, no unit
#    moved: ἐξέδυσαν = strip off, ἐνέδυσαν = clothe/dress.
#  - "and led him away him to crucify him." stuttered: ἀπήγαγον and αὐτὸν both
#    carried the "him".  ἀπήγαγον now reads "led", αὐτὸν "him away".
CHAPTER = "Matthew 27"
SECTION = 2
BLOCKS = [
    (7, 12, [(7, None), (10, None), (11, "company"), (8, None), (9, "him.")]),
    (50, 51, [(50, "struck him")]),
    (58, 60, [(58, "they stripped"), (59, "him of")]),
    (62, 64, [(62, "dressed"), (63, "him in")]),
    (67, 69, [(67, "led"), (68, "him away")]),
]
