#assignment
people = 20
cats = 30
dogs = 15


if people != cats:
    print "Too many cats! The world is doomed!"

#it still works.
if not(people > cats):
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"


dogs += 5

if people > dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
     #if there are 5 indents, it`ll still work, but not when there`s no indent.
     print "People are less than or equal to dogs."

#build a brunch to decide weather to run the commands next.
if people == dogs:
    print "People are dogs."
