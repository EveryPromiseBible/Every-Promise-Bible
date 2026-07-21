# -*- coding: utf-8 -*-
# Luke 4 §2 — two defects.
#
# 1. (97) "to a woman a widow." — two nouns in apposition with no join.
#    χήραν takes "who was a widow"; γυναῖκα is untouched. Gloss only, no
#    reorder. -> "to a woman who was a widow."
# 2. (118-122) "And all in the synagogue were filled with rage hearing these
#    things, and rising up, they drove him..." — the participle trails the main
#    verb and reads as a dangling afterthought. Move it in front:
#    "And all in the synagogue, hearing these things, were filled with rage,
#    and rising up, they drove him...". Pure reorder; the comma that closed
#    "these things," is now supplied by τῇ συναγωγῇ and θυμοῦ instead.
CHAPTER = "Luke 4"
SECTION = 2
BLOCKS = [
    (97, 98, [
        (97, "who was a widow."),    # χήραν
    ]),
    (118, 123, [
        (118, "the synagogue,"),     # τῇ συναγωγῇ
        (121, None),                 # ἀκούοντες    hearing
        (122, None),                 # ταῦτα        these things,
        (119, None),                 # ἐπλήσθησαν   were filled
        (120, "with rage,"),         # θυμοῦ
    ]),
]
