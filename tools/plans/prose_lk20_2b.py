# -*- coding: utf-8 -*-
# Luke 20:21 reads "and you do not receive a face, but you teach the way of God
# in truth." "Receive a face" is not English and an ordinary reader cannot
# recover the sense from it.
#
# λαμβάνειν πρόσωπον is a Semitism (Hebrew nasa panim, "lift the face") meaning
# to judge by a person's standing rather than the merits -- to show partiality.
# It is a fixed idiom, not a compositional phrase, which is why word-for-word
# glossing fails here.
#
# This is a thought-for-thought translation, so an idiom is glossed as an idiom.
# The same call was already made elsewhere in this corpus, most recently at
# John 6:66 / 18:6, where εἰς τὰ ὀπίσω stopped being "to the things behind" and
# became "back".
#
# Gloss-only, no unit moves, and the two words split the idiom the way the idiom
# itself divides -- the verb carries the showing, the noun carries what is shown:
#   35 λαμβάνεις "receive"  -> "show"
#   36 πρόσωπον  "a face,"  -> "partiality,"
# οὐ (34) keeps "you do not" and still carries the negation.
#
# Result: "and you do not show partiality, but you teach the way of God in truth."
CHAPTER = "Luke 20"
SECTION = 2
BLOCKS = [
    (35, 37, [
        (35, "show"),           # λαμβάνεις
        (36, "partiality,"),    # πρόσωπον
    ]),
]
