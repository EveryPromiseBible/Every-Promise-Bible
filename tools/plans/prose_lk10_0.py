# -*- coding: utf-8 -*-
# Luke 10 §0 — three Greek-order defects, all object/adverbial before the
# imperative. All pure reorders; only punctuation moves between glosses.
#
# 1. (64-69) "and no one along the road greet." -> "and greet no one along the
#    road."
# 2. (96-99) "In that same house stay, eating and drinking..." -> "Stay in that
#    same house, eating and drinking..."
# 3. (171-173) "yet this know: that the kingdom of God has come near."
#    -> "yet know this: that the kingdom of God has come near."
CHAPTER = "Luke 10"
SECTION = 0
BLOCKS = [
    (64, 70, [
        (64, None),                  # καὶ          and
        (69, "greet"),               # ἀσπάσησθε
        (65, None),                  # μηδένα       no one
        (66, None),                  # κατὰ         along
        (67, None),                  # τὴν          the
        (68, "road."),               # ὁδὸν
    ]),
    (96, 100, [
        (99, "Stay"),                # μένετε
        (96, "in"),                  # ἐν
        (97, None),                  # αὐτῇ δὲ τῇ   that same
        (98, "house,"),              # οἰκίᾳ
    ]),
    (171, 174, [
        (171, None),                 # πλὴν         yet
        (173, "know"),               # γινώσκετε
        (172, "this:"),              # τοῦτο
    ]),
]
