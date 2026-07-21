# -*- coding: utf-8 -*-
# Luke 3 §1 — three defects, all Greek word order standing in English.
#
# 1. (29-31) "‘We have as father Abraham.’" -> "‘We have Abraham as father.’"
#    Pure reorder; the closing quote rides to the new last unit.
# 2. (105-111) "Nothing more than what has been appointed to you collect."
#    The imperative πράσσετε was stranded at the end. -> "Collect nothing more
#    than what has been appointed to you." Reorder; the opening quote moves
#    onto πράσσετε and the closing quote onto ὑμῖν.
# 3. (125-126) "No one extort by violence, nor accuse falsely" — μηδένα is the
#    object, not the subject, so this reads as an address to "no one".
#    -> "Extort from no one, nor accuse falsely". The negation stays on
#    μηδένα ("no one") where the Greek puts it.
CHAPTER = "Luke 3"
SECTION = 1
BLOCKS = [
    (29, 32, [
        (29, None),                  # ἔχομεν      ‘We have
        (31, "Abraham"),             # τὸν Ἀβραάμ
        (30, "as father.’"),         # Πατέρα
    ]),
    (105, 112, [
        (111, "“Collect"),           # πράσσετε
        (105, "nothing"),            # Μηδὲν
        (106, None),                 # πλέον       more
        (107, None),                 # παρὰ        than
        (108, None),                 # τὸ          what
        (109, None),                 # διατεταγμένον has been appointed
        (110, "to you.”"),           # ὑμῖν
    ]),
    (125, 127, [
        (126, "“Extort from"),       # διασείσητε
        (125, "no one,"),            # Μηδένα
    ]),
]
