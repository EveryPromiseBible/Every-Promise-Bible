# -*- coding: utf-8 -*-
# Matthew 26 §1:
#  - "For a beautiful work she has done for me." -> "For she has done a
#    beautiful work for me."  Pure reorder, no gloss changed.
#  - "For always the poor you have with you, but me not always you have."
#    -> "For the poor you always have with you, but me you do not always
#    have."  πάντοτε keeps "always" (with the subject pulled in on the first
#    one, as the corpus does), ἔχετε keeps "have", οὐ takes "you do not".
CHAPTER = "Matthew 26"
SECTION = 1
BLOCKS = [
    (45, 51, [(45, None), (48, None), (46, None), (47, None), (49, None),
              (50, None)]),
    (51, 61, [(51, None), (53, None), (52, "you always"), (54, "have"),
              (55, None), (56, None), (57, None), (58, "you do not"),
              (59, None), (60, "have.")]),
]
