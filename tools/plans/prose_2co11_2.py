# -*- coding: utf-8 -*-
# 2 Corinthians 11:12 read: "...to cut off the opportunity of those who want an
# opportunity to be found, in what they boast about, just as we are."
# The purpose clause has collapsed: "to be found" reads as the complement of
# "want an opportunity", and "in what they boast about, just as we are" is left
# dangling. Greek is ἵνα ἐν ᾧ καυχῶνται εὑρεθῶσιν καθὼς καὶ ἡμεῖς — "so that in
# what they boast about they may be found just as we are."
# Fix: move the ἵνα-clause head in front and put εὑρεθῶσιν after καυχῶνται.
# Gloss changes:
#   9  ἀφορμήν  "an opportunity" -> "an opportunity,"  (comma only)
#   11 ἐν       "in" -> ""  folded; its sense is carried by the ἐν-ᾧ idiom on 12
#   12 ἵνα ᾧ    "what" -> "so that in what"  — ἵνα was previously UNGLOSSED;
#               this unit holds both tokens, so "so that" (ἵνα) + "what" (ᾧ) is
#               a more honest cover of the pair than the bare "what" it had.
#   13 καυχῶνται "they boast about," -> "they boast about"  (comma only)
#   10 εὑρεθῶσιν "to be found," -> "they may be found"  — aor. pass. subjunctive,
#               so a finite subjunctive is closer than the infinitive it had.
CHAPTER = "2 Corinthians 11"
SECTION = 2
BLOCKS = [
    (9, 17, [
        (9,  "an opportunity,"),      # ἀφορμήν
        (11, ""),                     # ἐν — folded
        (12, "so that in what"),      # ἵνα ᾧ
        (13, "they boast about"),     # καυχῶνται
        (10, "they may be found"),    # εὑρεθῶσιν
        (14, None),                   # καθὼς — "just"
        (15, None),                   # καὶ — "as"
        (16, None),                   # ἡμεῖς — "we are."
    ]),
]
