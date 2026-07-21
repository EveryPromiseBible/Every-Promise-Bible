# -*- coding: utf-8 -*-
# Acts 4 §0 read "…did you do this, you?" — the emphatic subject pronoun ὑμεῖς was
# left stranded after the object, producing a stutter. This gives
# "…did you do this?"
#
# Anchoring: English forces the periphrastic past "did … do" to split around its
# subject, so ὑμεῖς now carries "did you" (ὑμεῖς = "you"; "did" is the auxiliary
# English requires next to the subject) and ἐποιήσατε carries "do". τοῦτο keeps
# "this" and takes the question mark and closing quote from ὑμεῖς.
CHAPTER = "Acts 4"
SECTION = 0
BLOCKS = [
    (111, 114, [
        (113, "did you"),   # ὑμεῖς
        (111, "do"),        # ἐποιήσατε
        (112, "this?”"),    # τοῦτο — now ends the question
    ]),
]
