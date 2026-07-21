# -*- coding: utf-8 -*-
# John 13:28 read "Now this no one of those reclining knew as to what he said to
# him." The object is fronted ahead of subject and verb, so the reader has to
# reassemble the sentence. Now: "Now no one of those reclining knew this— as to
# what he said to him."
# One gloss edit, punctuation only:
#   111 τοῦτο "this" -> "this—"  (it now closes the main clause and introduces
#                                 the indirect question that follows)
# Nothing else changes; every other word stays on its own Greek word.
CHAPTER = "John 13"
SECTION = 2
BLOCKS = [
    (110, 120, [
        (110, None),       # δὲ           — Now
        (112, None),       # οὐδεὶς       — no one
        (113, None),       # τῶν          — of those
        (114, None),       # ἀνακειμένων  — reclining
        (115, None),       # ἔγνω         — knew
        (111, "this—"),    # τοῦτο
        (116, None),       # πρὸς         — as to
        (117, None),       # τί           — what
        (118, None),       # εἶπεν        — he said
        (119, None),       # αὐτῷ         — to him.
    ]),
]
