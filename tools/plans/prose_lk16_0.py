# -*- coding: utf-8 -*-
# Luke 16 §0 read "for either the one he will hate and the other he will love,
# or to one he will hold fast and the other he will despise." — Greek order
# (τὸν ἕνα μισήσει … τοῦ ἑτέρου καταφρονήσει), object before verb four times.
# Pure reorder to English verb-object order:
#   "for either he will hate the one and he will love the other, or he will
#    hold fast to one and he will despise the other."
# No gloss is re-anchored: every verb keeps its own English, every article and
# numeral keeps its own. Only two punctuation marks migrate:
#   241 ἕτερον "other" -> "other,"   (takes the comma before "or")
#   242 ἀγαπήσει "he will love," -> "he will love"
#   248 ἑτέρου "other" -> "other."   (now sentence-final)
#   249 καταφρονήσει "he will despise." -> "he will despise"
CHAPTER = "Luke 16"
SECTION = 0
BLOCKS = [
    (235, 250, [
        (235, None),              # ἢ γὰρ          for either
        (238, None),              # μισήσει        he will hate
        (236, None),              # τὸν            the
        (237, None),              # ἕνα            one
        (239, None),              # καὶ            and
        (242, "he will love"),    # ἀγαπήσει
        (240, None),              # τὸν            the
        (241, "other,"),          # ἕτερον
        (243, None),              # ἢ              or
        (245, None),              # ἀνθέξεται      he will hold fast
        (244, None),              # ἑνὸς           to one
        (246, None),              # καὶ            and
        (249, "he will despise"), # καταφρονήσει
        (247, None),              # τοῦ            the
        (248, "other."),          # ἑτέρου
    ]),
]
