print "You enter a dark room with three doors. Do you go through door #1, door #2 or door #3?"

door = raw_input('>')

if door == "1":
    print "There`s a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away."%bear

#the number followed must add ' ' or " ".
elif door == '2':
    print "You stare into the endless abyss at Cthulhu`s retina."
    print "1. Buleberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")

    if insanity == "1" or "2":     
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity prots your eyes into a pool of muck. Good job!"
        
elif door == "3":
    print "Aha, that`s noting but one person in the room."
    print "who do you want to meet in this moment?"
    people = raw_input("> ")
    
    #remember the ':', and be sure there are a four-space indent. 
    if people == ("lk"):
        print "Oh, you meet the most handsome guy in the world? \nI can`t believe it! You survived!"
    else: 
        print "Oh, %s is not the correct preson, he/she can`t save you, I`m sorry that you have to go die.\n\n\tBOOM!\n"%people
    
        
else:
   print "You stumble around and fall on a knife and die. Good job!"
                      
