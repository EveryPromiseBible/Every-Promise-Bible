# -*- coding: utf-8 -*-
# Acts 7 §0 read "…they will be enslaved I will judge,’ I, God, said;". The
# emphatic ἐγώ that belongs with κρινῶ ("κρινῶ ἐγώ" = "I myself will judge") had
# been left behind the closing quote, where it read as a stray apposition to
# "God". This gives "…they will be enslaved I myself will judge,’ God said;".
#
# Anchoring: ἐγώ now carries the emphatic subject "I myself"; κρινῶ carries
# "will judge" plus the comma and closing quote it already held; θεὸς is "God"
# with the stray comma removed; εἶπεν keeps "said;".
CHAPTER = "Acts 7"
SECTION = 0
BLOCKS = [
    (134, 139, [
        (135, "I myself"),        # ἐγώ
        (134, "will judge,’"),    # κρινῶ
        (136, None),              # ὁ — folded
        (137, "God"),             # θεὸς — comma removed
        (138, None),              # εἶπεν — "said;"
    ]),
]
