# -*- coding: utf-8 -*-
# Mark 12:7 read "But those tenants to one another said," — Greek order, the
# speech verb stranded after its prepositional phrase.
# This gives "But those tenants said to one another,".
# Pure reorder; the only gloss edits move the comma to the new final unit.
CHAPTER = "Mark 12"
SECTION = 0
BLOCKS = [
    (84, 87, [
        (86, "said"),            # εἶπαν ὅτι — loses the comma
        (84, None),              # πρὸς — to
        (85, "one another,"),    # ἑαυτοὺς — takes the comma
    ]),
]
