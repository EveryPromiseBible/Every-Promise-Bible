# -*- coding: utf-8 -*-
# Mark 3:28 read "that all will be forgiven the sons of men, the sins and the
# slanders, whatever they may blaspheme" — Greek order, with the subject
# (the sins and slanders) stranded after the verb and the indirect object.
# This gives "that all the sins and the slanders, whatever they may blaspheme,
# will be forgiven the sons of men".
# Pure reorder; the only gloss edits are punctuation:
#   112 βλασφημήσωσιν  ";" -> "," (the clause now continues into the verb)
#   107 τῶν ἀνθρώπων   "," -> ";" (the sentence-half now ends here)
# Every English word stays on its own Greek word.
CHAPTER = "Mark 3"
SECTION = 3
BLOCKS = [
    (104, 113, [
        (104, None),                 # πάντα — "all"
        (108, None),                 # τὰ ἁμαρτήματα — "the sins"
        (109, None),                 # καὶ — "and"
        (110, None),                 # αἱ βλασφημίαι — "the slanders,"
        (111, None),                 # ὅσα ἐὰν — "whatever"
        (112, "they may blaspheme,"),# βλασφημήσωσιν
        (105, None),                 # ἀφεθήσεται — "will be forgiven"
        (106, None),                 # τοῖς υἱοῖς — "the sons"
        (107, "of men;"),            # τῶν ἀνθρώπων
    ]),
]
