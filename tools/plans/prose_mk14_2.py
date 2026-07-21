# -*- coding: utf-8 -*-
# Mark 14:37 read "Were you not strong enough one hour to stay awake?" — Greek
# order, the infinitive stranded after its own time phrase.
# This gives "Were you not strong enough to stay awake one hour?"
# Pure reorder; the only gloss edits move the question mark to the new last unit.
CHAPTER = "Mark 14"
SECTION = 2
BLOCKS = [
    (160, 164, [
        (160, None),              # ἴσχυσας — strong enough
        (163, "to stay awake"),   # γρηγορῆσαι — loses the question mark
        (161, None),              # μίαν — one
        (162, "hour?"),           # ὥραν — takes the question mark
    ]),
]
