# -*- coding: utf-8 -*-
# Matthew 21 §0 — four Greek-order sentences:
#  - "if anyone to you says anything"     -> "if anyone says anything to you,"
#  - "the Lord of them has need"          -> "the Lord has need of them,"
#  - "placed on them their cloaks"        -> "placed their cloaks on them,"
#  - "when he entered he into Jerusalem"  -> "when he entered into Jerusalem"
#    (genitive absolute εἰσελθόντος αὐτοῦ: αὐτοῦ now carries "he", the
#     participle carries "entered" — the duplicated "he" is gone.)
# All reorders; the only gloss edits move a comma.
CHAPTER = "Matthew 21"
SECTION = 0
BLOCKS = [
    (36, 41, [(36, None), (37, None), (39, None), (40, "anything"), (38, "to you,")]),
    (42, 47, [(42, None), (43, None), (45, None), (46, "need"), (44, "of them,")]),
    (89, 93, [(89, None), (92, "their cloaks"), (90, None), (91, "them,")]),
    (133, 138, [(133, None), (135, "when he"), (134, "entered"),
                (136, None), (137, None)]),
]
