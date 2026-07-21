# -*- coding: utf-8 -*-
# Romans 16 §3 read: "Gaius, who has been a host to me and to the whole church,
# sends his greetings. To you." A full stop landed inside the clause, leaving
# "To you." as a two-word fragment sentence.
# ὑμᾶς is simply the object of ἀσπάζεται — the same pair already reads "sends
# his greetings to you," at units 3-4 of this section. Punctuation and the stray
# capital only; nothing moves and neither gloss changes its sense.
CHAPTER = "Romans 16"
SECTION = 3
BLOCKS = [
    (27, 29, [
        (27, "sends his greetings"),  # ἀσπάζεται
        (28, "to you."),              # ὑμᾶς
    ]),
]
