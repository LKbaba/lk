#the define of the FUNC
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #get the cheese in
    print "You have %d cheeses!"%cheese_count
    #get the crackers in 
    print "You have %d boxes of crackers!"%boxes_of_crackers
    #nothing but print
    print "Man that`s enough for a party!"
    #to get to next row.
    print "Get a blanket.\n"
    
    
#print
print "We can just give the function numbers directly:"
#to run the FUNC first
cheese_and_crackers(20, 30)


#just print
print "OR, we can use variables from our script:"
#the assignment
amount_of_cheese = 10
amount_of_crackers = 50

#call the FUNC with variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)



#just print
print "We can even do math inside too:"
#to add the math into FUNC
cheese_and_crackers(10 + 20, 5 + 6)


#just print
print "And we can combine the two, variables and math:"

#to run the FUNC with both variables and math
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)
