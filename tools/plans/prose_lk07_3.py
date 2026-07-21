# -*- coding: utf-8 -*-
# Luke 7 §3 — five defects.
#
# 1. (52)  "she was kissing warmly his feet" — adverb stranded after the verb.
#    καταφιλέω is one word meaning "kiss warmly/fervently", so the whole gloss
#    stays on it: "she was warmly kissing".
# 2. (68)  "the Pharisee ... said within himself, saying," — doubled speech
#    verb. λέγων folded (the corpus folds these elsewhere).
# 3. (96-99) "And he: “Teacher, say it,” he says." — a colon standing in for a
#    verb, then a second speech verb trailing after the quotation. Reordered to
#    "And he says, “Teacher, say it.”" — ὁ δέ keeps "And he", φησίν keeps
#    "says", and the full stop moves inside the closing quotation mark.
# 4. (177) Same adverb problem as (1): "has not stopped kissing warmly my feet"
#    -> "has not stopped warmly kissing my feet".
# 5. (202) "But to whom little is forgiven, loves little." — the relative has
#    no antecedent, so the sentence has no subject. ᾧ δὲ takes the antecedent
#    English requires: "But the one to whom".
CHAPTER = "Luke 7"
SECTION = 3
BLOCKS = [
    (52, 53, [
        (52, "she was warmly kissing"),   # κατεφίλει
    ]),
    (68, 69, [
        (68, ""),                         # λέγων — doubled speech verb, folded
    ]),
    (96, 100, [
        (96, "And he"),                   # ὁ δέ
        (99, "says,"),                    # φησίν
        (97, None),                       # Διδάσκαλε  “Teacher,
        (98, "say it.”"),                 # εἰπέ
    ]),
    (177, 178, [
        (177, "warmly kissing"),          # καταφιλοῦσά
    ]),
    (202, 203, [
        (202, "But the one to whom"),     # ᾧ δὲ
    ]),
]
