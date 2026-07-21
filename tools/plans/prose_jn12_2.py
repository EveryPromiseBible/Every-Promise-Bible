# -*- coding: utf-8 -*-
# John 12:22 read "Andrew comes and Philip, and they tell Jesus." The second
# subject was left stranded after the verb (Greek puts the singular ἔρχεται with
# the first of a compound subject). Now "Andrew and Philip come, and they tell
# Jesus."
# Gloss edits:
#   40 Φίλιππος "Philip," -> "Philip"  (comma moves off; it is no longer clause-final)
#   38 ἔρχεται  "comes"   -> "come,"   (still the verb of coming; English agrees
#                                       with the compound subject, and it now
#                                       carries the comma before "and they tell")
CHAPTER = "John 12"
SECTION = 2
BLOCKS = [
    (37, 41, [
        (37, None),        # Ἀνδρέας   — Andrew
        (39, None),        # καὶ       — and
        (40, "Philip"),    # Φίλιππος
        (38, "come,"),     # ἔρχεται
    ]),
]
