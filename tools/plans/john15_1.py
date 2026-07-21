# -*- coding: utf-8 -*-
# John 15 §1 — Remain in My Love
# DOCTRINE: keeps 15:9 "Just as the Father loved me, I also have loved
# you"; 15:12 "This is my commandment: that you love one another"; 15:13
# "Greater love has no one than this, that someone should lay down his
# life for his friends"; 15:16 "You did not choose me, but I chose you."
CHAPTER = "John 15"
SECTION = 1
BLOCKS = [
    # "Just as the Father loved me, I also have loved you.
    (0, 8, [(0,"“Just as"),(3,"the"),(4,"Father"),(1,"loved"),(2,"me,"),(5,"I also"),(7,"have loved"),(6,"you.")]),
    # Remain in my love.  (fold two articles)
    (8, 14, [(8,"Remain"),(9,"in"),(13,"my"),(11,"love."),(10,""),(12,"")]),
    # If you keep my commandments,  (fold article)
    (14, 19, [(14,"If"),(18,"you keep"),(17,"my"),(16,"commandments,"),(15,"")]),
    # in my love—  (fold article)
    (20, 24, [(20,"in"),(23,"my"),(22,"love—"),(21,"")]),
    # just as I have kept my Father's commandments  (fold two articles)
    (24, 32, [(24,"just as"),(25,"I"),(31,"have kept"),(30,"my"),(29,"Father's"),(27,"commandments"),(26,""),(28,"")]),
    # and remain in his love.  (fold article)
    (32, 38, [(32,"and"),(33,"remain"),(35,"in"),(34,"his"),(37,"love."),(36,"")]),
    # so that my joy may be in you,  (fold two articles)
    (41, 49, [(41,"so that"),(45,"my"),(43,"joy"),(42,""),(44,""),(48,"may be"),(46,"in"),(47,"you,")]),
    # and your joy may be made full.  (fold article)
    (49, 54, [(49,"and"),(52,"your"),(51,"joy"),(50,""),(53,"may be made full.")]),
    # my commandment:  (fold two articles)
    (56, 60, [(59,"my"),(57,"commandment:"),(56,""),(58,"")]),
    # Greater love than this no one has:
    (66, 71, [(66,"Greater"),(68,"love"),(67,"than this"),(69,"no one"),(70,"has:")]),
    # that someone should lay down his life for his friends.  (fold two articles)
    (71, 81, [(71,"that"),(72,"someone"),(76,"should lay down"),(75,"his"),(74,"life"),(73,""),(77,"for"),(80,"his"),(79,"friends."),(78,"")]),
    # You are my friends
    (81, 85, [(81,"You"),(84,"are"),(83,"my"),(82,"friends")]),
    # what his master is doing;  (fold article)
    (100,105,[(100,"what"),(102,"his"),(104,"master"),(103,""),(101,"is doing;")]),
    # from my Father  (fold article)
    (112,116,[(112,"from"),(115,"my"),(114,"Father"),(113,"")]),
    # You did not choose me,
    (118,122,[(119,"You"),(118,"did not"),(121,"choose"),(120,"me,")]),
    # so that you should go and bear fruit,
    (129,135,[(129,"so that"),(130,"you"),(131,"should go"),(132,"and"),(134,"bear"),(133,"fruit,")]),
    # and your fruit should remain—  (fold article)
    (135,140,[(135,"and"),(138,"your"),(137,"fruit"),(136,""),(139,"should remain—")]),
    # in my name  (fold article)
    (145,149,[(145,"in"),(148,"my"),(147,"name"),(146,"")]),
]
