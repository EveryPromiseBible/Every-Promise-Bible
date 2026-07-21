# -*- coding: utf-8 -*-
# Acts 21:38 read "led out into the wilderness the four thousand men of the
# assassins?" -- Greek order (ἐξαγαγὼν εἰς τὴν ἔρημον τοὺς τετρακισχιλίους
# ἄνδρας τῶν σικαρίων); the object trails the adverbial and the question mark
# lands four words late. Reordered to "led out the four thousand men of the
# assassins into the wilderness?"
# Pure reorder -- no gloss reassigned. Only the closing "?" and quotation mark
# move from τῶν σικαρίων (no longer last) to τὴν ἔρημον (now last).
CHAPTER = "Acts 21"
SECTION = 4
BLOCKS = [
    (29, 35, [
        (29, None),                       # ἐξαγαγὼν            "led out"
        (32, None),                       # τοὺς τετρακισχιλίους "the four thousand"
        (33, None),                       # ἄνδρας              "men"
        (34, "of the assassins"),         # τῶν σικαρίων
        (30, None),                       # εἰς                 "into"
        (31, "the wilderness?”"),         # τὴν ἔρημον
    ]),
]
