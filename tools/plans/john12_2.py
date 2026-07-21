# -*- coding: utf-8 -*-
# John 12 §2 — Unless a Grain of Wheat Falls (12:20-36)
# DOCTRINE: keeps 12:23 "the hour that the Son of Man may be glorified";
# 12:28 "Father, glorify your name!"; 12:31-32 "the ruler of this world
# will be cast out... if I am lifted up from the earth, will draw all to
# myself"; 12:34 "the Son of Man must be lifted up."
CHAPTER = "John 12"
SECTION = 2
BLOCKS = [
    # Now there were some Greeks among those going up
    (0, 7, [(1,"Now"),(0,"there were"),(3,"some"),(2,"Greeks"),(4,"among"),(5,"those"),(6,"going up")]),
    # Then these men came
    (12, 15, [(13,"Then"),(12,"these men"),(14,"came")]),
    # "Sir, we want to see Jesus."  (fold em-dash placeholder)
    (25, 30, [(25,"“Sir,"),(26,"we want"),(29,"to see"),(27,""),(28,"Jesus.”")]),
    # Philip comes and tells Andrew;  (fold two em-dash placeholders)
    (30, 37, [(32,"Philip"),(31,""),(30,"comes"),(33,"and"),(34,"tells"),(35,""),(36,"Andrew;")]),
    # Andrew comes and Philip, and they tell Jesus.  (fold em-dash placeholder)
    (37, 45, [(38,"Andrew"),(37,"comes"),(39,"and"),(40,"Philip,"),(41,"and"),(42,"they tell"),(43,""),(44,"Jesus.")]),
    # And Jesus  (fold em-dash placeholder)
    (45, 48, [(45,""),(46,"And"),(47,"Jesus")]),
    # "The hour has come that the Son of Man may be glorified.
    (51, 60, [(52,"“The"),(53,"hour"),(51,"has come"),(54,"that"),(56,"the"),(57,"Son"),(58,"of"),(59,"Man"),(55,"may be glorified.")]),
    # the grain of wheat,  (fold article)
    (65, 69, [(65,"the"),(66,"grain"),(67,"of"),(68,"wheat,")]),
    # it remains alone;
    (74, 77, [(74,"it"),(76,"remains"),(75,"alone;")]),
    # it bears much fruit.
    (79, 82, [(81,"it bears"),(79,"much"),(80,"fruit.")]),
    # The one loving his life loses it;  (fold article)
    (82, 89, [(82,"The one"),(83,"loving"),(86,"his"),(85,"life"),(84,""),(87,"loses"),(88,"it;")]),
    # and the one hating his life in this world will keep it for eternal life.  (fold article + em-dash placeholder)
    (89,104,[(89,"and"),(90,"the one"),(91,"hating"),(94,"his"),(93,"life"),(92,""),(95,"in"),(98,"this"),(97,"world"),(96,""),(102,"will keep"),(103,"it"),(99,"for"),(101,"eternal"),(100,"life.")]),
    # If anyone serves me, let him follow me;
    (104,110,[(104,"If"),(106,"anyone"),(107,"serves"),(105,"me,"),(109,"let him follow"),(108,"me;")]),
    # and where I am, there also my servant will be.  (fold two articles)
    (110,121,[(110,"and"),(111,"where"),(113,"I"),(112,"am,"),(114,"there"),(115,"also"),(119,"my"),(117,"servant"),(116,""),(118,""),(120,"will be.")]),
    # If anyone serves me, the Father will honor him.
    (121,129,[(121,"If"),(122,"anyone"),(124,"serves"),(123,"me,"),(127,"the"),(128,"Father"),(125,"will honor"),(126,"him.")]),
    # my soul  (fold article)
    (130,133,[(132,"my"),(131,"soul"),(130,"")]),
    # from this hour'?  (fold article)
    (140,144,[(140,"from"),(143,"this"),(142,"hour’?"),(141,"")]),
    # to this hour.  (fold article)
    (148,152,[(148,"to"),(151,"this"),(150,"hour."),(149,"")]),
    # glorify your name!  (fold article)
    (153,157,[(153,"glorify"),(154,"your"),(156,"name!”"),(155,"")]),
    # Then a voice came out of heaven:  (fold em-dash placeholder)
    (157,163,[(158,"Then"),(159,"a voice"),(157,"came"),(160,"out of"),(161,""),(162,"heaven:")]),
    # Then the crowd, the one standing and hearing, was saying
    (168,176,[(169,"Then"),(168,"the"),(170,"crowd,"),(171,"the one"),(172,"standing"),(173,"and"),(174,"hearing,"),(175,"was saying")]),
    # "An angel has spoken to him."
    (180,183,[(180,"“An angel"),(182,"has spoken"),(181,"to him.”")]),
    # Jesus answered and said,
    (183,187,[(184,"Jesus"),(183,"answered"),(185,"and"),(186,"said,")]),
    # has this voice come,
    (190,194,[(193,"has"),(192,"this"),(191,"voice"),(190,"come,")]),
    # Now is the judgment of this world;
    (197,203,[(197,"Now"),(199,"is"),(198,"the judgment"),(200,"of"),(202,"this"),(201,"world;")]),
    # now the ruler of this world will be cast out.  (fold pleonastic "outside")
    (203,211,[(203,"now"),(204,"the"),(205,"ruler"),(206,"of"),(208,"this"),(207,"world"),(209,"will be cast out."),(210,"")]),
    # will draw all to myself.
    (217,221,[(218,"will draw"),(217,"all"),(219,"to"),(220,"myself.”")]),
    # Now this he was saying,
    (221,224,[(222,"Now"),(221,"this"),(223,"he was saying,")]),
    # Then the crowd answered him,
    (229,234,[(230,"Then"),(232,"the"),(233,"crowd"),(229,"answered"),(231,"him,")]),
    # the Christ remains forever—  (idiom: to the age)
    (240,246,[(240,"the"),(241,"Christ"),(242,"remains"),(245,"forever—"),(243,""),(244,"")]),
    # and how do you say that the Son of Man must be lifted up?  (fold redundant subject)
    (246,257,[(246,"and"),(247,"how"),(248,"do you say"),(249,""),(250,"that"),(253,"the"),(254,"Son"),(255,"of"),(256,"Man"),(251,"must"),(252,"be lifted up?")]),
    # Who is this Son of Man?  (fold article)
    (257,264,[(257,"Who"),(258,"is"),(259,"this"),(260,""),(261,"Son"),(262,"of"),(263,"Man?”")]),
    # Then Jesus said to them,  (fold em-dash placeholder)
    (264,269,[(265,"Then"),(268,"Jesus"),(267,""),(264,"said"),(266,"to them,")]),
    # "Still a little time the light is among you.
    (269,277,[(269,"“Still"),(270,"a little"),(271,"time"),(272,"the"),(273,"light"),(276,"is"),(274,"among"),(275,"you.")]),
    # Walk while you have the light,
    (277,282,[(277,"Walk"),(278,"while"),(281,"you have"),(279,"the"),(280,"light,")]),
    # so that darkness may not overtake you;
    (282,287,[(282,"so that"),(284,"darkness"),(286,"may not overtake"),(283,""),(285,"you;")]),
    # While you have the light,
    (297,301,[(297,"While"),(300,"you have"),(298,"the"),(299,"light,")]),
    # so that you may become sons of light.
    (305,309,[(305,"so that"),(308,"you may become"),(306,"sons"),(307,"of light.”")]),
    # These things Jesus spoke,
    (309,312,[(309,"These things"),(311,"Jesus"),(310,"spoke,")]),
]
