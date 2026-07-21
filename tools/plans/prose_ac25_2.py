# -*- coding: utf-8 -*-
# Acts 25:15,17-18 -- two stumbles in Festus's speech.
# (a) "laid information, asking against him a sentence." is Greek order
#     (αἰτούμενοι κατ’ αὐτοῦ καταδίκην): the object lands after the adverbial.
#     Reordered to "asking for a sentence against him". Pure reorder except
#     42 αἰτούμενοι "asking" -> "asking for" (the middle αἰτέομαι is exactly
#     "ask for", and English needs the preposition once the object follows) and
#     the full stop moving from καταδίκην, no longer last, to αὐτοῦ, now last --
#     and it becomes a comma, because...
# (b) "...a sentence. To whom I answered" left the relative οὓς stranded as a
#     fragment. Comma, not full stop; 46/47 decapitalised to "to whom".
CHAPTER = "Acts 25"
SECTION = 2
BLOCKS = [
    (42, 48, [
        (42, "asking for"),    # αἰτούμενοι
        (45, "a sentence"),    # καταδίκην
        (43, None),            # κατ’   "against"
        (44, "him,"),          # αὐτοῦ
        (46, "to"),            # πρὸς
        (47, "whom"),          # οὓς
    ]),
    # (c) Acts 25:18 -- "ordered the man brought. About whom the accusers..."
    # strands the relative οὗ the same way. Comma, not full stop.
    (79, 82, [
        (79, "brought,"),      # ἀχθῆναι
        (80, "about"),         # περὶ
        (81, "whom"),          # οὗ
    ]),
]
