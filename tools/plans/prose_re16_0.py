# -*- coding: utf-8 -*-
# Revelation 16 §0 — two defects.
#
# (1) 16:3 read "and every living soul died, the things that were in the sea."
#     The subject phrase τὰ ἐν τῇ θαλάσσῃ is left trailing after the verb in
#     Greek order, so it lands in English as a bolted-on "the things that were
#     in the sea" that disagrees with the singular "soul" it is describing.
#     Fix: move the phrase in front of the verb and fold the article.
#       τὰ  "the things" -> ""  (folded article — the established convention;
#            the article's relative force is carried by "that" below)
#       ἐν  "that were in" -> "that was in"  (same supplied relative + copula it
#            already carried; only the number agrees with "soul" now)
#     Gives: "and every living soul that was in the sea died."
#
# (2) 16:7 read "true and just are the judgments of yours." "the judgments of
#     yours" is not English — a postposed genitive standing where a possessive
#     determiner belongs. Move σου in front of the noun and gloss it "your".
#       αἱ  "are the" -> "are"  (this unit already carried the supplied copula;
#            it keeps it. The definite article drops out of the English because
#            the possessive "your" now fills the determiner slot — which is what
#            the Greek article is doing here anyway.)
#       σου "of yours.”" -> "your"
#       κρίσεις "judgments" -> "judgments.”"  (the sentence-final period and the
#            closing quotation mark move with the word that is now last)
#     Gives: "true and just are your judgments.”"
CHAPTER = "Revelation 16"
SECTION = 0
BLOCKS = [
    (68, 76, [
        (68, None),            # πᾶσα — "every"
        (69, None),            # ζωῆς — "living"
        (70, None),            # ψυχὴ — "soul"
        (72, ""),              # τὰ — folded article
        (73, "that was in"),   # ἐν
        (74, None),            # τῇ — "the"
        (75, "sea"),           # θαλάσσῃ — was "sea." ; the full stop moves to "died."
        (71, "died."),         # ἀπέθανεν — now sentence-final
    ]),
    (134, 140, [
        (134, None),           # ἀληθιναὶ — "true"
        (135, None),           # καὶ — "and"
        (136, None),           # δίκαιαι — "just"
        (137, "are"),          # αἱ — keeps the supplied copula
        (139, "your"),         # σου
        (138, "judgments.”"),  # κρίσεις — takes the final punctuation
    ]),
]
