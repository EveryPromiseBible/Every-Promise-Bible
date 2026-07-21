# -*- coding: utf-8 -*-
# Mark 14:41 — ἀπέχει ("it is enough") was rendered BLANK while its gloss
# "That is enough!" sat on τὸ λοιπὸν ("for the rest / still"), whose own sense
# had been absorbed into Καθεύδετε ("Are you still sleeping").
# Give each word its own label.
CHAPTER = "Mark 14"
SECTION = 2
BLOCKS = [
    (209, 214, [
        (209, "“Are you sleeping"),   # Καθεύδετε
        (210, None),                 # καὶ — and
        (211, "resting"),            # ἀναπαύεσθε
        (212, "still?"),             # τὸ λοιπὸν
        (213, "That is enough!"),    # ἀπέχει
    ]),
]
