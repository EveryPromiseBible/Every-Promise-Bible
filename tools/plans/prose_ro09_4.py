# -*- coding: utf-8 -*-
# Romans 9 §4 read: "...where it was said to them, you are not my people, you,
# there they will be called children of the living God."
# The Greek is οὐ λαός μου ὑμεῖς — ὑμεῖς is the subject pronoun, but it sits
# after the predicate in Greek order, so English got a stranded, doubled "you,"
# on the far side of the phrase. A reader stops on it.
#
# Reorder only, within [20,23): ὑμεῖς moves to the front as the subject "you",
# Οὐ carries the negation "are not", λαός μου keeps "my people,".
# Each gloss still describes its own Greek word: ὑμεῖς = "you" (it was already
# glossed "you,"), Οὐ = "are not" (it was already the "not" of "you are not"),
# λαός μου = "my people," unchanged. Comma preserved on the phrase's last word.
CHAPTER = "Romans 9"
SECTION = 4
BLOCKS = [
    (20, 23, [
        (22, "you"),          # ὑμεῖς
        (20, "are not"),      # Οὐ
        (21, "my people,"),   # λαός μου
    ]),
]
