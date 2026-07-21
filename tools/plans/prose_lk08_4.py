# -*- coding: utf-8 -*-
# Luke 8 §4 — three defects.
#
# 1. (57-59) "And a woman being with a flow of blood for twelve years" — the
#    bare participle "being" plus "with" is not English. οὖσα ἐν ῥύσει is
#    "who had a flow"; the preposition ἐν is folded because "had" absorbs it.
# 2. (127-132) "trembling she came and falling down before him, she declared" —
#    inverted participle plus a redundant repeated subject. Reordered and the
#    duplicate pronoun dropped from ἀπήγγειλεν: "came trembling and falling
#    down before him, declared before all the people...".
# 3. (166) Recitative ὅτι before an opening quotation mark
#    ("saying, that “Your daughter has died"). Folded.
CHAPTER = "Luke 8"
SECTION = 4
BLOCKS = [
    (57, 60, [
        (57, "who had"),             # οὖσα
        (58, ""),                    # ἐν — preposition folded under "had"
        (59, "a flow"),              # ῥύσει
    ]),
    (127, 133, [
        (128, "came"),               # ἦλθεν       (was "she came")
        (127, None),                 # τρέμουσα    trembling
        (129, None),                 # καὶ         and
        (130, None),                 # προσπεσοῦσα falling down before
        (131, None),                 # αὐτῷ        him,
        (132, "declared"),           # ἀπήγγειλεν  (was "she declared")
    ]),
    (166, 167, [
        (166, ""),                   # ὅτι — recitative, folded
    ]),
]
