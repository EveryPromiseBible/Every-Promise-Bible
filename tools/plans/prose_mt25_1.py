# -*- coding: utf-8 -*-
# Matthew 25 §1:
#  - "over many things you I will put in charge." (twice) -> "I will set you
#    over many things."  Follows the Matthew 24 §5 precedent: καταστήσω already
#    means set/appoint, so it reads "I will set" and ἐπὶ keeps "over".
#  - "‘You wicked servant and lazy!" -> "‘You wicked and lazy servant!"
#    Pure reorder; only the "!" travels to the new last unit.
#  - "there there will be weeping" stuttered: ἐκεῖ already carries "there",
#    so ἔσται drops its expletive and reads "will be". No unit moved.
CHAPTER = "Matthew 25"
SECTION = 1
BLOCKS = [
    (101, 105, [(104, "I will set"), (103, "you"), (101, None),
                (102, "many things.")]),
    (140, 144, [(143, "I will set"), (142, "you"), (140, None),
                (141, "many things.")]),
    (189, 193, [(189, None), (191, None), (192, "lazy"), (190, "servant!")]),
    (249, 250, [(249, "will be")]),
]
