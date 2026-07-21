# -*- coding: utf-8 -*-
# Two matching defects in Mark 12 §2 — a manner adverb left in Greek position
# ahead of its verb.
#
# 1) Mark 12:28 read "seeing that well he had answered them,"
#    -> "seeing that he had answered them well,"
# 2) Mark 12:34 read "seeing him, that wisely he had answered,"
#    -> "seeing him, that he had answered wisely,"
#
# Both are pure reorders; the only gloss edits move the comma onto whichever
# unit now ends the clause.
CHAPTER = "Mark 12"
SECTION = 2
BLOCKS = [
    (9, 12, [
        (10, None),      # ἀπεκρίθη — he had answered
        (11, "them"),    # αὐτοῖς — loses the comma
        (9,  "well,"),   # καλῶς — takes the comma
    ]),
    (113, 115, [
        (114, "he had answered"),   # ἀπεκρίθη — loses the comma
        (113, "wisely,"),           # νουνεχῶς — takes the comma
    ]),
]
