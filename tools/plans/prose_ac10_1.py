# -*- coding: utf-8 -*-
# Acts 10 §1 read "…whether Simon the one called Peter here is lodging." — the
# adverb sat before the verb, in Greek order. This gives "…whether Simon the one
# called Peter is lodging here."
# Pure reorder; only the full stop moves to ἐνθάδε, which now ends the sentence.
CHAPTER = "Acts 10"
SECTION = 1
BLOCKS = [
    (151, 153, [
        (152, "is lodging"),  # ξενίζεται — full stop moves off
        (151, "here."),       # ἐνθάδε — now ends the sentence
    ]),
]
