# -*- coding: utf-8 -*-
# Matthew 27 §1:
#  - "how many things against you they testify?" -> "how many things they
#    testify against you?"  Pure reorder.
#  - "do you want I release to you" (twice) -> "do you want me to release to
#    you".  Gloss only; ἀπολύσω stays the release verb.
#  - "Have nothing to do with you and that righteous man," -> "Let there be
#    nothing between you and that righteous man,".  Gloss only: μηδὲν keeps
#    "nothing", the dative σοί reads "between you".
#  - "for many things I have suffered today" -> "for I have suffered many
#    things today".  Pure reorder.
#  - "but Jesus to destroy." -> "but to destroy Jesus."  Pure reorder.
#  - "And the governor answered, said to them," -> "answered and said to
#    them,".  Doubled speech verb; gloss only.
#  - "but Jesus, having flogged, he handed over" -> "but having flogged Jesus,
#    he handed over".  Pure reorder; the comma travels.
CHAPTER = "Matthew 27"
SECTION = 1
BLOCKS = [
    (32, 35, [(32, None), (34, "they testify"), (33, "against you?”")]),
    (71, 72, [(71, "me to release")]),
    (96, 105, [(96, "“Let there be nothing"), (97, "between you"), (98, None),
               (99, None), (100, None), (101, None), (103, None), (102, None),
               (104, None)]),
    (118, 121, [(118, None), (120, "to destroy"), (119, "Jesus.")]),
    (123, 125, [(123, "answered"), (124, "and said")]),
    (130, 131, [(130, "me to release")]),
    (195, 201, [(195, None), (197, "having flogged"), (196, "Jesus,"),
                (198, None), (199, None), (200, None)]),
]
