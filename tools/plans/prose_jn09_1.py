# -*- coding: utf-8 -*-
# John 9:16 read "This man is not from God— the man— because he does not keep
# the Sabbath." The trailing ὁ ἄνθρωπος was left as a dangling apposition, so
# the reader gets "the man" twice with nothing to attach it to. Reordered so the
# noun sits with its demonstrative: "This man is not from God, because he does
# not keep the Sabbath."
# This makes the anchoring MORE honest, not less:
#   52 οὗτος    "This man" -> "“This" (οὗτος is the demonstrative alone; it still
#                                      opens the speech, so it keeps the quote mark)
#   57 ἄνθρωπος "man—"     -> "man"   (now carries the noun it actually is)
#   56 ὁ        "the"      -> folded  (the article, per the usual convention)
#   55 θεοῦ     "God—"     -> "God,"  (dash becomes a comma; no dangling clause left)
CHAPTER = "John 9"
SECTION = 1
BLOCKS = [
    (52, 58, [
        (52, "“This"),     # οὗτος
        (56, ""),          # ὁ
        (57, "man"),       # ἄνθρωπος
        (53, None),        # Οὐκ ἔστιν — is not
        (54, None),        # παρὰ      — from
        (55, "God,"),      # θεοῦ
    ]),
]
