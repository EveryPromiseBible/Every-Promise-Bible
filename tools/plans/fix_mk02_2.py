# -*- coding: utf-8 -*-
# Mark 2:21 — glosses slid across the patch clause.
# τὸ καινὸν ("the new") carried "pulls away"; αἴρει ("takes away") carried "from";
# ἀπ' carried "it,"; αὐτοῦ ("it") carried "the new". Reordered so each gloss
# rides its own Greek. Prose unchanged.
CHAPTER = "Mark 2"
SECTION = 2
BLOCKS = [
    (64, 71, [
        (64, None),            # εἰ δὲ μή      — "otherwise,"
        (65, None),            # τὸ πλήρωμα    — "the patch"
        (67, "pulls away"),    # αἴρει
        (68, "from"),          # ἀπ’
        (69, "it,"),           # αὐτοῦ
        (66, "the new"),       # τὸ καινὸν
        (70, None),            # τοῦ παλαιοῦ   — "from the old,"
    ]),
]
