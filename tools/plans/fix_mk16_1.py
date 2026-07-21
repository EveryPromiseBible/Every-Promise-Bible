# -*- coding: utf-8 -*-
# Mark 16 shorter ending — Πάντα ("all") sat in a unit labelled only "And",
# while its gloss had drifted onto ἐξήγγειλαν ("they reported all").
# Reorder so πάντα … τὰ carries "all that" and the verb carries the verb.
CHAPTER = "Mark 16"
SECTION = 1
BLOCKS = [
    (0, 4, [
        (2, "And they reported"),   # ἐξήγγειλαν
        (1, "briefly"),             # συντόμως
        (0, "all that"),            # Πάντα δὲ τὰ
        (3, "had been commanded"),  # παρηγγελμένα
    ]),
]
