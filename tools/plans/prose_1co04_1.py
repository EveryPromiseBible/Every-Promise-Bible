# -*- coding: utf-8 -*-
# 1 Corinthians 4:6 read "...so that you're not puffed up one for the one against
# the other." That is Greek order (ἵνα μὴ ... φυσιοῦσθε εἷς ὑπὲρ τοῦ ἑνὸς κατὰ
# τοῦ ἑτέρου) with the subject εἷς stranded after the verb, so the sentence has
# no visible subject until three words too late. Reordering to subject-verb
# gives: "so that not one of you is puffed up in favour of the one against the
# other."
# Gloss changes, all honest:
#   18 ἵνα μὴ    "so that" -> "so that not"  (μή is the negative; it moves off
#                the verb and onto its own particle, where it belongs)
#   19 φυσιοῦσθε "you're not puffed up" -> "of you is puffed up" (2nd person
#                plural passive; "of you" is the plural subject agreement, the
#                negation has moved to ἵνα μὴ)
#   21 ὑπὲρ      "for" -> "in favour of"  (ὑπέρ + genitive = on behalf of)
# 20, 22, 23, 24 keep their glosses unchanged.
CHAPTER = "1 Corinthians 4"
SECTION = 1
BLOCKS = [
    (18, 25, [
        (18, "so that not"),        # ἵνα μὴ
        (20, None),                 # εἷς — "one"
        (19, "of you is puffed up"),# φυσιοῦσθε
        (21, "in favour of"),       # ὑπὲρ
        (22, None),                 # τοῦ ἑνὸς — "the one"
        (23, None),                 # κατὰ — "against"
        (24, None),                 # τοῦ ἑτέρου — "the other."
    ]),
]
