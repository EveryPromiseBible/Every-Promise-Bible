# -*- coding: utf-8 -*-
# Acts 8 §2 (the Isaiah quotation) read "His generation who will describe?" —
# object-first Greek order. This gives "Who will describe his generation?"
# Pure reorder; only the capital and the question mark move to the words that
# now open and close the question.
CHAPTER = "Acts 8"
SECTION = 2
BLOCKS = [
    (143, 148, [
        (146, "Who"),           # τίς — now opens the question
        (147, "will describe"), # διηγήσεται — question mark moves off
        (145, None),            # τὴν — folded
        (143, "his"),           # αὐτοῦ — no longer sentence-initial
        (144, "generation?"),   # γενεὰν — now closes the question
    ]),
]
