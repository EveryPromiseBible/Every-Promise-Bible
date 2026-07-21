# -*- coding: utf-8 -*-
# Matthew 7:9 + 7:12 — the last Greek leak in the corpus, plus heavy gloss drift.
#
# 7:12 read: "for this and you also sums up the Law and the Prophets. Οὗτος γάρ"
#   - raw Greek "Οὗτος γάρ" was sitting on the ENGLISH line of the last unit
#   - οὕτως ("so/thus") was labelled "for this" — that is οὗτος, a different word
#   - αὐτοῖς ("to them") was labelled "also"; καὶ/ὑμεῖς were stranded mid-clause
#   - οἱ ἄνθρωποι (subject of ποιῶσιν) was labelled "to others", which is αὐτοῖς
#   - a surplus ἐστιν sat in the 7:12 region; SBLGNT places it at 7:9
#     (ἢ τίς ἐστιν ἐξ ὑμῶν ἄνθρωπος), where the section had no verb at all.
#
# Fix: move the stray ἐστιν unit back to 7:9 and gloss it "Is there"; rebuild
# 7:12 in honest reading order. Greek multiset is unchanged (both edits are
# inside this one section), so the SBLGNT count is untouched while the token
# now sits in its right clause.
CHAPTER = "Matthew 7"
SECTION = 1

BLOCKS = [
    # ---- 7:9-7:12 ----------------------------------------------------------
    (21, 69,
     [
         (68, "Is there"),   # ἐστιν  — moved back to 7:9 from the 7:12 region
         (21, "anyone"),     # ἢ τίς
         (22, "among you"),  # ἐξ ὑμῶν ἄνθρωπος
     ]
     # ὃν is the relative pronoun ("whom his son will ask"); it was labelled
     # a bare "if", which left the new clause ungrammatical.
     + [(23, "who, if")]
     # 24-54 untouched: "your son asks for bread, will give him a stone? ...
     # how much more will your Father in heaven give good gifts to those who
     # ask him!"
     + [(i, None) for i in range(24, 55)]
     + [
         (55, None),                  # οὖν              | So
         (56, None),                  # (filler)         | in
         (57, None),                  # Πάντα            | everything,
         (60, "whatever"),            # ὅσα
         (61, "you would have"),      # ἐὰν θέλητε ἵνα
         (59, "others"),              # οἱ ἄνθρωποι
         (62, None),                  # ποιῶσιν          | do
         (63, None),                  # ὑμῖν             | to you,
         (64, "in the same way"),     # οὕτως
         (66, "you"),                 # ὑμεῖς
         (65, "also"),                # καὶ
         (58, "should do"),           # ποιεῖτε
         (67, "to them."),            # αὐτοῖς
     ]),

    # ---- 7:12b -------------------------------------------------------------
    (69, 73, [
        (72, "For this is"),   # οὗτος γάρ ἐστιν — was the leaked "Οὗτος γάρ"
        (69, None),            # ὁ νόμος       | the Law
        (70, None),            # καὶ           | and
        (71, None),            # οἱ προφῆται   | the Prophets.
    ]),
]
