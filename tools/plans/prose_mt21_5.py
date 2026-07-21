# -*- coding: utf-8 -*-
# Matthew 21 §5 — six Greek-order sentences, all pure reorders
# (gloss edits are punctuation only, moving a comma/period to the new last unit):
#  - "dug in it a winepress"                    -> "dug a winepress in it"
#  - "he sent to them his son"                  -> "he sent his son to them"
#  - "from the Lord this came"                  -> "this came from the Lord"
#  - "that will be taken away from you the kingdom of God"
#                                               -> "that the kingdom of God will
#                                                   be taken away from you"
#  - "they knew that about them he was speaking" -> "...that he was speaking about them"
#  - "because as a prophet him they held"        -> "because they held him as a prophet"
CHAPTER = "Matthew 21"
SECTION = 5
BLOCKS = [
    (13, 17, [(13, None), (16, None), (14, None), (15, None)]),
    (60, 66, [(60, None), (61, None), (64, None), (65, "son"),
              (62, None), (63, "them,")]),
    (135, 138, [(137, "this came"), (135, None), (136, "the Lord,")]),
    (147, 153, [(147, None), (151, None), (152, None),
                (148, None), (149, None), (150, None)]),
    (178, 182, [(178, None), (181, "he was speaking"), (179, None), (180, "them.")]),
    (188, 193, [(188, None), (192, "they held"), (191, None),
                (189, None), (190, "a prophet.")]),
]
