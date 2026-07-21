# -*- coding: utf-8 -*-
# ἐνενήκοντα ἐννέα ("ninety nine"): ἐνενήκοντα carried the whole "ninety-nine"
# while ἐννέα was blank, twice in this section. Clicking ἐνενήκοντα ("ninety")
# reported "ninety-nine". Split; the full value stays in the prose.
CHAPTER = "Luke 15"
SECTION = 1
BLOCKS = [
    (15, 17, [(15, "ninety"), (16, "nine")]),
    (73, 75, [(73, "ninety"), (74, "nine")]),
]
