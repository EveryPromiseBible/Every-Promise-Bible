# -*- coding: utf-8 -*-
# Acts 8 §0 — two small prose defects, both gloss-only (no reorder).
#
# 1) "as they heard and seeing the signs that he was doing" — βλέπειν is the
#    second of two parallel infinitives under ἐν τῷ … αὐτούς, so it must match
#    ἀκούειν ("heard"), not drift into a participle. -> "saw".
#
# 2) "For many of those having unclean spirits crying out with a loud voice, were
#    coming out;" — the comma sat before the verb instead of around the
#    participial phrase, so the sentence read as if the people came out. Moving
#    the comma to πνεύματα makes "crying out with a loud voice" parenthetical:
#    "For many of those having unclean spirits, crying out with a loud voice,
#    were coming out;".
CHAPTER = "Acts 8"
SECTION = 0
BLOCKS = [
    (95, 96, [
        (95, "saw"),        # βλέπειν
    ]),
    (104, 105, [
        (104, "spirits,"),  # πνεύματα
    ]),
]
