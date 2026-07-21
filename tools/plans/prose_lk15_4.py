# -*- coding: utf-8 -*-
# Luke 15 §4 — six defects, all Greek word order left standing in English.
#
# BLOCK 1 (10,12): "as coming he drew near to the house" — a bare participle
#   in front of the finite verb. Gloss-only, no reorder:
#     10 ἐρχόμενος "coming"     -> "he came and"   (same verb ἔρχομαι)
#     11 ἤγγισεν   "he drew near" -> "drew near"   (subject moves to the
#        participle so the two verbs coordinate; the verb is unchanged)
#   Gives "and as he came and drew near to the house, he heard music…"
#
# BLOCK 2 (24,28): "he was inquiring what might be these things." — Greek
#   order (τί ἂν εἴη ταῦτα). Pure reorder to "what these things might be."
#   The full stop moves from ταῦτα onto the new final unit εἴη.
#
# BLOCK 3 (30,32): "And he said to him that ‘Your brother has come…". This is
#   recitative ὅτι, which marks a DIRECT quotation and has no English word;
#   "that" in front of an opening quotation mark is a reader stumble. Folded,
#   per the project's convention for untranslatable particles, and the comma
#   that introduces the speech moves onto αὐτῷ.
#
# BLOCK 4 (77,82): "and to me never did you give a young goat" — the dative
#   fronted in Greek order. Pure reorder to "and never did you give me a young
#   goat", keeping the emphatic inversion that matches the parallel clause
#   "never did I disobey your command" just before it.
#     78 ἐμοὶ "to me" -> "me"  (same pronoun; it is now the indirect object of
#        "give", which in English takes no preposition in this position)
#
# BLOCK 5 (82,88): "so that with my friends I might celebrate." — Greek order.
#   Pure reorder to "so that I might celebrate with my friends."
#   The full stop moves from εὐφρανθῶ onto the new final word φίλων.
#
# BLOCK 6 (101,106): "you killed for him the fattened calf!’" — Greek order
#   (ἔθυσας αὐτῷ τὸν σιτευτὸν μόσχον). Pure reorder to "you killed the
#   fattened calf for him!’". The exclamation mark AND the closing single
#   quotation mark travel together from μόσχον onto the new final unit αὐτῷ,
#   so the son's speech still closes.
CHAPTER = "Luke 15"
SECTION = 4
BLOCKS = [
    (10, 12, [
        (10, "he came and"),   # ἐρχόμενος
        (11, "drew near"),     # ἤγγισεν
    ]),
    (24, 28, [
        (24, None),            # τί     what
        (27, "these things"),  # ταῦτα
        (25, None),            # ἂν     might
        (26, "be."),           # εἴη
    ]),
    (30, 32, [
        (30, "to him,"),       # αὐτῷ
        (31, ""),              # ὅτι    recitative — folded
    ]),
    (77, 82, [
        (77, None),   # καὶ       and
        (79, None),   # οὐδέποτε  never
        (80, None),   # ἔδωκας    did you give
        (78, "me"),   # ἐμοὶ
        (81, None),   # ἔριφον    a young goat
    ]),
    (82, 88, [
        (82, None),                 # ἵνα        so that
        (87, "I might celebrate"),  # εὐφρανθῶ
        (83, None),                 # μετὰ       with
        (84, None),                 # μου        my
        (86, None),                 # τῶν        (folded)
        (85, "friends."),           # φίλων
    ]),
    (101, 106, [
        (101, None),           # ἔθυσας     you killed
        (103, None),           # τὸν        the
        (104, None),           # σιτευτὸν   fattened
        (105, "calf"),         # μόσχον
        (102, "for him!’"),    # αὐτῷ
    ]),
]
