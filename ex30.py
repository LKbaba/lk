#assignment
people = 30 
cars = 40 
buses = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We shsould not take the cars."
else:
    print "We can`t decide."

if buses > cars:
    print "That`s too many buses."
#anther situation.
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can`t decide."
    
#comparing
if people > buses and buses <cars:
    print "Alright, let`s just take the buses."
#'else' like, the others situation.
else:
    #print
    print "Fine, let`s stay home then."                
