# -*- coding: utf-8 -*-
# Luke 12 §2 — two Greek-order defects.
#
# 1. (68-72) "why about the rest are you anxious?" -> "why are you anxious
#    about the rest?" Pure reorder; the question mark moves onto λοιπῶν.
# 2. (95-110) "But if the grass in a field, which is here today, and tomorrow
#    is thrown into an oven, God so clothes, how much more you" — the subject
#    and verb are stranded at the end behind sixteen words of object, so the
#    reader reaches "God so clothes," with no idea what is being clothed.
#    -> "But if God so clothes the grass in a field, which is here today, and
#    tomorrow is thrown into an oven, how much more you". Pure reorder; the
#    only gloss edit is dropping the comma from ἀμφιέζει, which is no longer
#    the end of the clause.
CHAPTER = "Luke 12"
SECTION = 2
BLOCKS = [
    (68, 73, [
        (68, None),                  # τί           why
        (72, "are you anxious"),     # μεριμνᾶτε
        (69, None),                  # περὶ         about
        (70, None),                  # τῶν          the
        (71, "rest?"),               # λοιπῶν
    ]),
    (95, 111, [
        (95, None),                  # εἰ δὲ        But if
        (107, None),                 # ὁ            (folded)
        (108, None),                 # θεὸς         God
        (109, None),                 # οὕτως        so
        (110, "clothes"),            # ἀμφιέζει
        (96, None),                  # τὸν          the
        (97, None),                  # χόρτον       grass
        (98, None),                  # ἐν           in
        (99, None),                  # ἀγρῷ         a field,
        (100, None),                 # ὄντα         which is here
        (101, None),                 # σήμερον      today,
        (102, None),                 # καὶ          and
        (103, None),                 # αὔριον       tomorrow
        (104, None),                 # βαλλόμενον   is thrown
        (105, None),                 # εἰς          into
        (106, None),                 # κλίβανον     an oven,
    ]),
]
