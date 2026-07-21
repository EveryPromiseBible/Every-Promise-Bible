# -*- coding: utf-8 -*-
# Mark 15:39 read "And seeing the centurion who was standing opposite him, that
# in this way he breathed his last, he said, ..." — Greek order puts the
# participle first, so an English reader takes "the centurion" as the OBJECT of
# "seeing" rather than its subject. That is a meaning error, not just a stumble.
# This gives "And seeing that in this way he breathed his last, the centurion
# who was standing opposite him said, ..."
# Pure reorder; the only gloss edits are punctuation and a now-redundant
# supplied pronoun:
#   81 αὐτοῦ  "him," -> "him"  (no comma before the verb)
#   85 εἶπεν  "he said," -> "said,"  (the subject is now stated: the centurion)
CHAPTER = "Mark 15"
SECTION = 3
BLOCKS = [
    (76, 86, [
        (76, None),        # ἰδὼν δὲ — And seeing
        (82, None),        # ὅτι — that
        (83, None),        # οὕτως — in this way
        (84, None),        # ἐξέπνευσεν — he breathed his last,
        (77, None),        # ὁ — the
        (78, None),        # κεντυρίων — centurion
        (79, None),        # ὁ παρεστηκὼς — who was standing
        (80, None),        # ἐξ ἐναντίας — opposite
        (81, "him"),       # αὐτοῦ
        (85, "said,"),     # εἶπεν
    ]),
]
