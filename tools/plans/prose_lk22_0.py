# -*- coding: utf-8 -*-
# Luke 22 §0 — two defects.
#
# BLOCK 1 (83,84): read "saying, “Going, prepare for us the Passover…" — a
#   bare aorist participle where English needs a coordinate imperative.
#   Πορευθέντες is attendant-circumstance to the imperative ἑτοιμάσατε, so
#   "Go and" is the same verb (πορεύομαι) in the form English uses. Gloss-only;
#   the opening quotation mark stays on it.
#
# BLOCK 2 (125,129): read "‘Says to you the Teacher: Where is the guest
#   room…" — Greek order (Λέγει σοι ὁ διδάσκαλος), verb before subject, which
#   in English reads as a broken clause. Pure reorder to
#   "‘The Teacher says to you: Where is the guest room…".
#   No gloss is re-anchored; the opening single quotation mark moves onto the
#   new first word and the colon onto the new last word:
#     127 ὁ          "the"       -> "‘The"
#     128 διδάσκαλος "Teacher:"  -> "Teacher"
#     125 Λέγει      "‘Says"     -> "says"
#     126 σοι        "to you"    -> "to you:"
CHAPTER = "Luke 22"
SECTION = 0
BLOCKS = [
    (83, 84, [
        (83, "“Go and"),   # Πορευθέντες
    ]),
    (125, 129, [
        (127, "‘The"),      # ὁ
        (128, "Teacher"),   # διδάσκαλος
        (125, "says"),      # Λέγει
        (126, "to you:"),   # σοι
    ]),
]
