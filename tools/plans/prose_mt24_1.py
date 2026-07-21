# -*- coding: utf-8 -*-
# Matthew 24 §1
#  - "For false messiahs will arise and false prophets," -> "For false messiahs
#    and false prophets will arise,". Pure reorder; comma moves.
#  - "‘Look, in the wilderness he is,’" -> "‘Look, he is in the wilderness,’".
#    Pure reorder; the closing quote travels to the new last unit.
CHAPTER = "Matthew 24"
SECTION = 1
BLOCKS = [
    (102, 106, [(102, None), (104, None), (105, "false prophets"),
                (103, "will arise,")]),
    (124, 128, [(124, None), (127, "he is"), (125, None),
                (126, "the wilderness,’")]),
]
