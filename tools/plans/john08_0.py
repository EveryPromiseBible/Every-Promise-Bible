# -*- coding: utf-8 -*-
# John 8 §0 — I Am the Light of the World
# DOCTRINE: keeps "I am the light of the world" (8:12); "unless you
# believe that I am, you will die in your sins" (8:24); "When you lift up
# the Son of Man, then you will know that I am" (8:28) — the egō eimi
# sayings rendered "I am".
CHAPTER = "John 8"
SECTION = 0
BLOCKS = [
    # Then again Jesus spoke to them,  (fold em-dash placeholder)
    (0, 6, [(1,"Then"),(0,"again"),(5,"Jesus"),(4,""),(3,"spoke"),(2,"to them,")]),
    # the light of life.
    (23, 27, [(23,"the"),(24,"light"),(25,"of"),(26,"life.”")]),
    # Then the Pharisees said to him,
    (27, 32, [(28,"Then"),(30,"the"),(31,"Pharisees"),(27,"said"),(29,"to him,")]),
    # "You testify about yourself;
    (32, 36, [(32,"“You"),(35,"testify"),(33,"about"),(34,"yourself;")]),
    # your testimony is not true.  (fold article)
    (36, 41, [(38,"your"),(37,"testimony"),(36,""),(39,"is not"),(40,"true.”")]),
    # Jesus answered and said to them,
    (41, 46, [(42,"Jesus"),(41,"answered"),(43,"and"),(44,"said"),(45,"to them,")]),
    # my testimony is true,  (fold article)
    (51, 56, [(55,"my"),(54,"testimony"),(53,""),(52,"is"),(51,"true,")]),
    # You judge according to the flesh;
    (71, 76, [(71,"You"),(75,"judge"),(72,"according to"),(73,"the"),(74,"flesh;")]),
    # I judge no one.
    (76, 80, [(76,"I"),(78,"judge"),(79,"no one."),(77,"")]),
    # my judgment is true,  (fold two articles)
    (85, 91, [(88,"my"),(86,"judgment"),(85,""),(87,""),(90,"is"),(89,"true,")]),
    # because I am not alone,
    (91, 94, [(91,"because"),(93,"I am not"),(92,"alone,")]),
    # And in your law now it is written  (fold two articles)
    (102,109,[(102,"in"),(107,"your"),(104,"law"),(103,""),(106,""),(105,"now"),(108,"it is written")]),
    # that the testimony of two people is true.
    (109,116,[(109,"that"),(112,"the"),(113,"testimony"),(110,"of two"),(111,"people"),(115,"is"),(114,"true.")]),
    # and the One who sent me— the Father— testifies about me.
    (122,130,[(122,"and"),(126,"the One"),(127,"who sent"),(128,"me—"),(129,"the Father—"),(123,"testifies"),(124,"about"),(125,"me.”")]),
    # Then they were saying to him,
    (130,133,[(131,"Then"),(130,"they were saying"),(132,"to him,")]),
    # your Father?  (fold article)
    (135,138,[(137,"your"),(136,"Father?”"),(135,"")]),
    # Jesus answered,
    (138,140,[(139,"Jesus"),(138,"answered,")]),
    # "You know neither me nor my Father.  (fold article)
    (140,147,[(142,"“You know"),(140,"neither"),(141,"me"),(143,"nor"),(146,"my"),(145,"Father."),(144,"")]),
    # If you had known me,
    (147,150,[(147,"If"),(149,"you had known"),(148,"me,")]),
    # you would also have known my Father.  (fold article)
    (150,156,[(154,"you would"),(150,"also"),(155,"have known"),(153,"my"),(152,"Father.”"),(151,"")]),
    # These words  (fold article)
    (156,159,[(156,"These"),(157,""),(158,"words")]),
    # because his hour had not yet come.
    (171,177,[(171,"because"),(176,"his"),(175,"hour"),(174,""),(172,"had not yet"),(173,"come.")]),
    # Then again he said to them,
    (177,181,[(178,"Then"),(179,"again"),(177,"he said"),(180,"to them,")]),
    # in your sin you will die.  (fold article)
    (187,192,[(187,"in"),(190,"your"),(189,"sin"),(188,""),(191,"you will die.")]),
    # Then the Jews were saying,
    (198,202,[(199,"Then"),(200,"the"),(201,"Jews"),(198,"were saying,")]),
    # "You are from below;  (fold article)
    (216,221,[(216,"“You"),(220,"are"),(217,"from"),(219,"below;"),(218,"")]),
    # I am from above.  (fold article)
    (221,226,[(221,"I"),(225,"am"),(222,"from"),(224,"above."),(223,"")]),
    # You are of this world;  (fold article)
    (226,232,[(226,"You"),(231,"are"),(227,"of"),(228,"this"),(230,"world;"),(229,"")]),
    # I am not of this world.  (fold article)
    (232,238,[(232,"I"),(233,"am not"),(234,"of"),(237,"this"),(236,"world."),(235,"")]),
    # Then I said to you
    (238,241,[(239,"Then"),(238,"I said"),(240,"to you")]),
    # in your sins;  (fold article)
    (243,247,[(243,"in"),(246,"your"),(245,"sins;"),(244,"")]),
    # in your sins.  (fold article)
    (253,257,[(253,"in"),(256,"your"),(255,"sins.”"),(254,"")]),
    # Then they were saying to him,
    (257,260,[(258,"Then"),(257,"they were saying"),(259,"to him,")]),
    # Jesus said to them,  (fold em-dash placeholder)
    (263,267,[(266,"Jesus"),(265,""),(263,"said"),(264,"to them,")]),
    # "What I have been telling you from the beginning.  (fold emphatic conjunction)
    (267,272,[(268,"“What"),(269,""),(270,"I have been telling"),(271,"you"),(267,"from the beginning.")]),
    # Many things I have to say and to judge about you;
    (272,279,[(272,"Many things"),(273,"I have"),(276,"to say"),(277,"and"),(278,"to judge"),(274,"about"),(275,"you;")]),
    # but the One who sent me is true,
    (279,285,[(279,"but"),(280,"the One"),(281,"who sent"),(282,"me"),(284,"is"),(283,"true,")]),
    # They did not understand that he was speaking to them about the Father.
    (295,302,[(295,"They did not"),(296,"understand"),(297,"that"),(301,"he was speaking"),(300,"to them"),(298,"about the"),(299,"Father.")]),
    # Then Jesus said,  (fold em-dash placeholder)
    (302,306,[(303,"Then"),(305,"Jesus"),(304,""),(302,"said,")]),
    # but just as the Father taught me,
    (322,328,[(322,"but"),(323,"just as"),(326,"the"),(327,"Father"),(324,"taught"),(325,"me,")]),
    # And the One who sent me is with me.
    (330,337,[(330,"And"),(331,"the One"),(332,"who sent"),(333,"me"),(336,"is"),(334,"with"),(335,"me.")]),
    # He has not left me alone,
    (337,341,[(337,"He has not"),(338,"left"),(339,"me"),(340,"alone,")]),
    # because I always do the things pleasing to him.
    (341,348,[(341,"because"),(342,"I"),(347,"always"),(346,"do"),(343,"the things"),(344,"pleasing"),(345,"to him.”")]),
]
