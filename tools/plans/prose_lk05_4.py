# -*- coding: utf-8 -*-
# Luke 5 §4 — three defects.
#
# 1. (55) Recitative ὅτι before an opening quotation mark
#    ("a parable to them, that “No one tearing off..."). Folded.
# 2. (66-71) "otherwise, both the new he will tear, and the patch from the new
#    will not match the old." — object before verb. -> "otherwise, he will tear
#    the new, and the patch...". The correlative καί ("both") is folded, since
#    with the verb fronted "both he will tear the new" no longer parses; the
#    second καί still carries "and".
# 3. (105-111) "But new wine into fresh wineskins must be put." — verb stranded
#    at the end. -> "But new wine must be put into fresh wineskins."
CHAPTER = "Luke 5"
SECTION = 4
BLOCKS = [
    (55, 56, [
        (55, ""),                    # ὅτι — recitative, folded
    ]),
    (66, 72, [
        (66, None),                  # εἰ δὲ μήγε   otherwise,
        (67, ""),                    # καὶ — correlative "both", folded
        (70, "he will tear"),        # σχίσει
        (68, None),                  # τὸ           the
        (69, "new,"),                # καινὸν
        (71, None),                  # καὶ          and
    ]),
    (105, 112, [
        (105, None),                 # ἀλλὰ         But
        (106, None),                 # νέον         new
        (107, None),                 # οἶνον        wine
        (111, "must be put"),        # βλητέον
        (108, None),                 # εἰς          into
        (109, None),                 # καινοὺς      fresh
        (110, "wineskins."),         # ἀσκοὺς
    ]),
]
