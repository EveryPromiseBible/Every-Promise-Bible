# -*- coding: utf-8 -*-
# Two Greek-order sentences in 1 Corinthians 8:7.
#
# BLOCK 1 — read "But not in everyone is this knowledge." (ἀλλ’ οὐκ ἐν πᾶσιν ἡ
# γνῶσις): the subject sits last, so the reader parses "not in everyone" as a
# fragment before the subject arrives. Reorder to subject-first gives
# "But this knowledge is not in everyone."
#   4 ἡ γνῶσις  "is this knowledge." -> "this knowledge is"  (the copula is
#     supplied in both versions — Greek has none here — it just travels with the
#     subject noun phrase now instead of trailing it)
#   3 πᾶσιν     "everyone" -> "everyone."  (sentence-final full stop moves here)
#
# BLOCK 2 — read "by the habit until now of the idol": the genitive τοῦ εἰδώλου
# is split from the noun it modifies by "until now", the classic postposed
# genitive. Reordering it back against τῇ συνηθείᾳ gives "by their habit of the
# idol until now".
#   7  τῇ συνηθείᾳ  "by the habit" -> "by their habit"  (the article τῇ is
#      possessive here, as the following αὐτῶν συνείδησις confirms)
#   10 τοῦ εἰδώλου  "of the idol," -> "of the idol"  (comma moves to the new
#      end of the phrase)
#   9  ἄρτι        "now" -> "now,"
CHAPTER = "1 Corinthians 8"
SECTION = 2
BLOCKS = [
    (0, 5, [
        (0, None),                  # Ἀλλ’ — "But"
        (4, "this knowledge is"),   # ἡ γνῶσις
        (1, None),                  # οὐκ — "not"
        (2, None),                  # ἐν — "in"
        (3, "everyone."),           # πᾶσιν
    ]),
    (7, 11, [
        (7, "by their habit"),      # τῇ συνηθείᾳ
        (10, "of the idol"),        # τοῦ εἰδώλου
        (8, None),                  # ἕως — "until"
        (9, "now,"),                # ἄρτι
    ]),
]
