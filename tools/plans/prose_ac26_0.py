# -*- coding: utf-8 -*-
# Acts 26:2 read "I count myself fortunate that before you I am about today to
# make my defence" -- Greek order (ἐπὶ σοῦ μέλλων σήμερον ἀπολογεῖσθαι) left
# standing; "I am about today to make" splits the infinitive phrase and the
# reader has to back up. Reordered to "that I am about to make my defence
# before you today".
# Pure reorder except for where the supplied complementizer "that" sits: it was
# hung on ἐπὶ ("that before"), which is wrong -- ἐπὶ is only "before". It now
# sits on μέλλων, the participle that actually heads the clause. The comma
# before "especially" moves from ἀπολογεῖσθαι to σήμερον, now last.
CHAPTER = "Acts 26"
SECTION = 0
BLOCKS = [
    (25, 30, [
        (27, "that I am about"),      # μέλλων
        (29, "to make my defence"),   # ἀπολογεῖσθαι
        (25, "before"),               # ἐπὶ
        (26, None),                   # σοῦ      "you"
        (28, "today,"),               # σήμερον
    ]),
]
