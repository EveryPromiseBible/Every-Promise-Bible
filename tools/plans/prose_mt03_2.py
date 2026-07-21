# -*- coding: utf-8 -*-
# Matthew 3 §2: "Jesus replied, to him: 'let it be so now.'" — the stray comma
# splits the verb from its complement. Drop it: "Jesus replied to him:".
# Punctuation only; no reorder, no gloss change.
CHAPTER = "Matthew 3"
SECTION = 2
BLOCKS = [
    (24, 26, [
        (24, "replied"),   # ἀποκριθεὶς δὲ εἶπεν  (was "replied,")
        (25, None),        # πρὸς αὐτόν — to him:
    ]),
]
