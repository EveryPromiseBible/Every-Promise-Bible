# -*- coding: utf-8 -*-
# Luke 19 §1 — two defects.
#
# BLOCK 1 (122,125): read "And came the second, saying," — Greek order
#   (καὶ ἦλθεν ὁ δεύτερος), verb before subject where English has no reason
#   to invert. Pure reorder to "And the second came, saying,". Only the comma
#   moves, from δεύτερος onto ἦλθεν:
#     124 δεύτερος "second," -> "second"
#     122 ἦλθεν    "came"    -> "came,"
#
# BLOCK 2 (241,243): read "that to everyone the one having it will be given;"
#   — the articular participle rendered as a stranded appositive, so the
#   sentence has no readable subject. Gloss-only, no reorder:
#     241 τῷ      "the one"  -> "who"    (the article is the relative marker
#         of the participial phrase; "who" is what it does in English here)
#     242 ἔχοντι  "having"   -> "has,"   (same participle, finite in English
#         because it now heads a relative clause)
#   Gives "that to everyone who has, it will be given; but from the one not
#   having, even what he has will be taken away." δοθήσεται is untouched.
CHAPTER = "Luke 19"
SECTION = 1
BLOCKS = [
    (122, 125, [
        (123, None),       # ὁ         the
        (124, "second"),   # δεύτερος
        (122, "came,"),    # ἦλθεν
    ]),
    (241, 243, [
        (241, "who"),      # τῷ
        (242, "has,"),     # ἔχοντι
    ]),
]
