# -*- coding: utf-8 -*-
# Matthew 8:8 gloss-drift fix. The labels were shifted one word off:
#   μου "you should come" | τὴν στέγην "my" | εἰσέλθῃς "roof;"
# Prose read fine ("that you should come under my roof") but every gloss sat on
# the wrong Greek word. Reorder the span so reading order is unchanged while each
# English chunk anchors to its correct word:
#   ἵνα "that" · εἰσέλθῃς "you should come" · ὑπὸ "under" · μου "my" · στέγην "roof;"
CHAPTER = "Matthew 8"
SECTION = 1
BLOCKS = [
    (36, 41, [
        (36, None),               # ἵνα -> "that"
        (40, "you should come"),   # εἰσέλθῃς -> the verb
        (38, None),               # ὑπὸ -> "under"
        (37, "my"),               # μου -> "my"
        (39, "roof;"),            # τὴν στέγην -> "roof;"
    ]),
]
