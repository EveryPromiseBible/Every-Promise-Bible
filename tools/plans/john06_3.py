# -*- coding: utf-8 -*-
# John 6 §3 — The Bread Is My Flesh (6:41-59)
# DOCTRINE: keeps "I am the bread of life / the living bread", "the bread
# I will give is my flesh, for the life of the world", "eat the flesh of
# the Son of Man and drink his blood", "the living Father sent me."
CHAPTER = "John 6"
SECTION = 3
BLOCKS = [
    # Then the Jews were grumbling about him
    (0, 6, [(1,"Then"),(2,"the"),(3,"Jews"),(0,"were grumbling"),(4,"about"),(5,"him")]),
    # the bread that came down out of heaven,  (fold em-dash placeholder)
    (10, 17, [(10,"the"),(11,"bread"),(12,"that"),(13,"came down"),(14,"out of"),(15,""),(16,"heaven,”")]),
    # "Is not this man Jesus, the son of Joseph,  (fold em-dash placeholder)
    (19, 26, [(19,"“Is not"),(20,"this man"),(21,""),(22,"Jesus,"),(23,"the"),(24,"son"),(25,"of Joseph,")]),
    # whose father and mother we know?  (fold redundant subject)
    (26, 34, [(26,"whose"),(29,""),(30,"father"),(31,"and"),(32,""),(33,"mother"),(27,""),(28,"we know?")]),
    # 'Out of heaven I have come down'?  (fold em-dash placeholder)
    (38, 42, [(38,"‘Out of"),(39,""),(40,"heaven"),(41,"I have come down’?”")]),
    # Jesus answered and said to them,
    (42, 47, [(43,"Jesus"),(42,"answered"),(44,"and"),(45,"said"),(46,"to them,")]),
    # the Father who sent me draws him—  (fold doubled article)
    (57, 64, [(57,"the"),(58,"Father"),(59,""),(60,"who sent"),(61,"me"),(62,"draws"),(63,"him—")]),
    # and I will raise him up on the last day.
    (64, 71, [(64,"and I"),(65,"will raise"),(66,"him up"),(67,"on"),(68,"the"),(69,"last"),(70,"day.")]),
    # 'And they will all be taught of God.'
    (76, 81, [(76,"‘And"),(77,"they will"),(78,"all"),(79,"be taught"),(80,"of God.’")]),
    # Everyone who has heard  (fold em-dash placeholder)
    (81, 84, [(81,"Everyone"),(82,""),(83,"who has heard")]),
    # Not that anyone has seen the Father—
    (92, 98, [(92,"Not"),(93,"that"),(97,"anyone"),(96,"has seen"),(94,"the"),(95,"Father—")]),
    # the One being from God;  (fold em-dash placeholder)
    (99,104,[(99,"the One"),(100,"being"),(101,"from"),(102,""),(103,"God;")]),
    # has eternal life.
    (114,117,[(114,"has"),(116,"eternal"),(115,"life.")]),
    # the bread of life.  (fold redundant article)
    (119,123,[(119,"the"),(120,"bread"),(121,"of"),(122,"life.")]),
    # Your fathers ate the manna in the wilderness and died.  (fold article)
    (123,134,[(125,"Your"),(124,"fathers"),(123,""),(126,"ate"),(130,"the"),(131,"manna"),(127,"in"),(128,"the"),(129,"wilderness"),(132,"and"),(133,"died.")]),
    # the bread that comes down out of heaven,  (fold em-dash placeholder)
    (136,143,[(136,"the"),(137,"bread"),(138,"that"),(142,"comes down"),(139,"out of"),(140,""),(141,"heaven,")]),
    # so that someone may eat of it and not die.
    (143,151,[(143,"so that"),(144,"someone"),(147,"may eat"),(145,"of"),(146,"it"),(148,"and"),(149,"not"),(150,"die.")]),
    # the living bread,  (fold doubled article)
    (153,157,[(153,"the"),(156,"living"),(154,"bread,"),(155,"")]),
    # the One having come down out of heaven.  (fold em-dash placeholder)
    (157,162,[(157,"the One"),(161,"having come down"),(158,"out of"),(159,""),(160,"heaven.")]),
    # of this bread,  (fold em-dash placeholder)
    (165,169,[(165,"of"),(166,"this"),(167,""),(168,"bread,")]),
    # he will live forever;  (idiom: to the age)
    (169,173,[(169,"he will live"),(170,""),(171,""),(172,"forever;")]),
    # and the bread indeed that I will give is my flesh, for the life of the world.
    (173,189,[(173,"and"),(174,"the"),(175,"bread"),(176,"indeed"),(177,"that"),(178,"I"),(179,"will give"),(183,"is"),(182,"my"),(181,"flesh,"),(180,""),(184,"for"),(185,"the"),(188,"life"),(186,"of the"),(187,"world.”")]),
    # Then the Jews were fighting with one another,
    (189,195,[(190,"Then"),(193,"the"),(194,"Jews"),(189,"were fighting"),(191,"with"),(192,"one another,")]),
    # "How can this man give us his flesh to eat?"
    (196,205,[(196,"“How"),(197,"can"),(198,"this man"),(200,"give"),(199,"us"),(203,"his"),(202,"flesh"),(201,""),(204,"to eat?”")]),
    # Then Jesus said to them,  (fold em-dash placeholder)
    (205,210,[(206,"Then"),(209,"Jesus"),(208,""),(205,"said"),(207,"to them,")]),
    # drink his blood,  (fold article)
    (223,227,[(223,"drink"),(224,"his"),(226,"blood,"),(225,"")]),
    # The one gnawing my flesh and drinking my blood  (fold two articles)
    (232,242,[(232,"The one"),(233,"gnawing"),(234,"my"),(236,"flesh"),(235,""),(237,"and"),(238,"drinking"),(239,"my"),(241,"blood"),(240,"")]),
    # has eternal life,
    (242,245,[(242,"has"),(244,"eternal"),(243,"life,")]),
    # and I will raise him up on the last day.
    (245,251,[(245,"and I"),(246,"will raise"),(247,"him up"),(248,"on the"),(249,"last"),(250,"day.")]),
    # For my flesh is true food,
    (251,257,[(251,"For"),(253,"my"),(252,"flesh"),(255,"is"),(254,"true"),(256,"food,")]),
    # and my blood is true drink.  (fold article)
    (257,264,[(257,"and"),(260,"my"),(259,"blood"),(258,""),(262,"is"),(261,"true"),(263,"drink.")]),
    # The one gnawing my flesh and drinking my blood  (fold two articles)
    (264,274,[(264,"The one"),(265,"gnawing"),(266,"my"),(268,"flesh"),(267,""),(269,"and"),(270,"drinking"),(271,"my"),(273,"blood"),(272,"")]),
    # remains in me,
    (274,277,[(276,"remains"),(274,"in"),(275,"me,")]),
    # Just as the living Father sent me,
    (280,286,[(280,"Just as"),(283,"the"),(284,"living"),(285,"Father"),(281,"sent"),(282,"me,")]),
    # so also the one gnawing me,
    (291,295,[(291,"so also"),(292,"the one"),(293,"gnawing"),(294,"me,")]),
    # the bread that came down out of heaven—
    (301,307,[(301,"the"),(302,"bread"),(303,"that"),(306,"came down"),(304,"out of"),(305,"heaven—")]),
    # not just as the fathers ate and died.
    (307,314,[(307,"not"),(308,"just as"),(310,"the"),(311,"fathers"),(309,"ate"),(312,"and"),(313,"died.")]),
    # The one gnawing this bread will live forever.  (fold em-dash placeholder + idiom)
    (314,323,[(314,"The one"),(315,"gnawing"),(316,"this"),(317,""),(318,"bread"),(319,"will live"),(320,""),(321,""),(322,"forever.”")]),
    # These things he said teaching in a synagogue in Capernaum.
    (323,330,[(323,"These things"),(324,"he said"),(327,"teaching"),(325,"in"),(326,"a synagogue"),(328,"in"),(329,"Capernaum.")]),
]
