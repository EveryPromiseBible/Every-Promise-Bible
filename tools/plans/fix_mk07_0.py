# -*- coding: utf-8 -*-
# Mark 7 §0 — #243-246: the verb ἐκπορεύεται ("goes out") was rendered as a bare
# em-dash placeholder while its sense "out" sat on the preposition εἰς. Reordered
# into English order so ἐκπορεύεται carries "goes out" and εἰς carries "into";
# the stray "—" between "latrine?”" and "(Thus he declared clean" disappears.
CHAPTER = "Mark 7"
SECTION = 0
BLOCKS = [
    (243, 247, [
        (243, None),        # καὶ — "and"
        (246, "goes out"),  # ἐκπορεύεται (was "—")
        (244, "into"),      # εἰς (was "out into")
        (245, None),        # τὸν ἀφεδρῶνα — "the latrine?”"
    ]),
]
