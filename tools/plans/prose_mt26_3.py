# -*- coding: utf-8 -*-
# Matthew 26 §3:
#  - "Where do you want we should prepare" -> "Where do you want us to
#    prepare".  Gloss only; ἑτοιμάσωμέν is still the 1pl "prepare", now in the
#    English infinitive the sentence requires.
#  - "The one who has dipped with me his hand in the bowl" -> "...his hand in
#    the bowl with me".  Pure reorder; only the comma travels.
#  - "if not had been born that man." -> "if that man had not been born."
#    Reorder; οὐκ takes "had not" (the corpus already reads οὐκ as "you did
#    not" etc.) and ἐγεννήθη keeps "been born".
#  - "drink from now of this fruit of the vine until that day" -> "drink of
#    this fruit of the vine from now until that day".  Pure reorder.
CHAPTER = "Matthew 26"
SECTION = 3
BLOCKS = [
    (8, 9, [(8, "us to prepare")]),
    (74, 80, [(74, None), (77, None), (78, None), (79, "the bowl"),
              (75, None), (76, "me,")]),
    (98, 105, [(98, None), (99, None), (100, None), (103, None), (104, "man"),
               (101, "had not"), (102, "been born.”")]),
    (165, 173, [(165, None), (166, None), (169, None), (170, None), (171, None),
                (172, None), (167, None), (168, None)]),
]
