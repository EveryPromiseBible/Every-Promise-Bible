# -*- coding: utf-8 -*-
# Matthew 6:14 — gloss drift. ὑμῖν (dative, "to you") was labelled "your" and
# pulled forward to head "your heavenly Father"; the real possessive ὑμῶν was
# stranded at the START of the next sentence as a bare capitalised "Your",
# producing the prose glitch "...forgive you. Your but if you do not forgive".
# Fix: ὑμῶν takes "your" (with ὁ πατὴρ), ὑμῖν takes the object "you.",
# the supplied filler carries the apodosis "then", and δὲ opens v15 as "But".
# Pure reorder plus honest relabelling of the two pronouns.
CHAPTER = "Matthew 6"
SECTION = 1
BLOCKS = [
    (116, 129, [
        (116, None),      # γὰρ                  | For
        (117, None),      # Ἐὰν                  | if
        (118, None),      # ἀφῆτε                | you forgive
        (119, None),      # τοῖς ἀνθρώποις       | other people
        (120, None),      # τὰ παραπτώματα αὐτῶν | when they sin against you,
        (126, "then"),    # (filler, supplied)
        (127, "your"),    # ὑμῶν
        (122, None),      # ὁ οὐράνιος           | heavenly
        (123, None),      # ὁ πατὴρ              | Father
        (124, None),      # καὶ                  | will also
        (125, None),      # ἀφήσει               | forgive
        (121, "you."),    # ὑμῖν
        (128, "But"),     # δὲ
    ]),
]
