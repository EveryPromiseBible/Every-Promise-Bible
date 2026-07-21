# -*- coding: utf-8 -*-
# Matthew 19 §3:
#  (a) "a rich person with difficulty will enter into the kingdom of heaven" —
#      adverb standing before the verb in Greek order. Reordered to
#      "a rich person will enter into the kingdom of heaven with difficulty".
#      Pure reorder.
#  (b) "Then Peter answered him, said," — doubled speech verb with no
#      conjunction. εἶπεν reglossed "and said,".
CHAPTER = "Matthew 19"
SECTION = 3
BLOCKS = [
    (9, 15, [
        (9, None),                  # πλούσιος — "a rich person"
        (11, None),                 # εἰσελεύσεται — "will enter"
        (12, None),                 # εἰς — "into"
        (13, None),                 # τὴν βασιλείαν — "the kingdom"
        (14, "of heaven"),          # τῶν οὐρανῶν
        (10, "with difficulty."),   # δυσκόλως
    ]),
    (57, 59, [
        (57, "him"),                # αὐτῷ
        (58, "and said,"),          # εἶπεν
    ]),
]
