# -*- coding: utf-8 -*-
# 1 Corinthians 10:22 currently ends: "Or are we provoking to jealousy the Lord?
# Are we are we provoking the Lord to jealousy?"
#
# That second sentence is GLOSS DRIFT, not a style problem. Paul's second
# question is μὴ ἰσχυρότεροι αὐτοῦ ἐσμέν; — "Are we stronger than he?" The
# glosses for ἰσχυρότεροι and αὐτοῦ were overwritten with a copy of the previous
# clause, producing the "Are we are we" stutter and losing the sentence
# entirely. (This was introduced by tools/plans/1cor10_2fix.py, which targeted
# indices 94/95 believing them to be παραζηλοῦμεν/τὸν κύριον. That old plan must
# not be applied again.)
#
# Gloss-only restoration, no reorder:
#   94 ἰσχυρότεροι  "are we provoking" -> "stronger"      (comparative of ἰσχυρός)
#   95 αὐτοῦ        "the Lord to jealousy?" -> "than he?" (genitive of comparison)
# 93 μὴ ἐσμεν keeps "Are we" — it is already correct.
# Gives: "Or are we provoking to jealousy the Lord? Are we stronger than he?"
CHAPTER = "1 Corinthians 10"
SECTION = 2
BLOCKS = [
    (94, 96, [
        (94, "stronger"),   # ἰσχυρότεροι
        (95, "than he?"),   # αὐτοῦ
    ]),
]
