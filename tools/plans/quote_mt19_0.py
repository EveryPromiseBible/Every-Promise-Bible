# -*- coding: utf-8 -*-
# Matthew 19 §0: three fixes.
#  (a) ORPHAN NESTED CLOSER — unit 54 ends "female,’" but no ‘ ever opened the
#      Genesis citation. Opens it at "made" (50), so the quoted span is
#      "‘made them male and female,’". (This is the section that also showed
#      1 open / 2 close on the SINGLE-quote count.)
#  (b) 44 "“Have you not read" never closed; narration resumes at 86 ("They say to
#      him"); closes after "separate." (85).
#  (c) 99 "“Moses ... permitted you" never closed; narration resumes at 132 ("The
#      disciples say to him"); closes after "commits adultery." (131).
CHAPTER = "Matthew 19"
SECTION = 0
BLOCKS = [
  (50, 51, [(50, "‘made")]),
  (85, 86, [(85, "separate.”")]),
  (131, 132, [(131, "commits adultery.”")]),
]
