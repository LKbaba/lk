def add(a, b):
    print "I know you want to add two of your age together, right?"
    print "Just wait a minute.\n"
    return a + b

your_age = raw_input("How old are you? >\n")

your_mother_age = raw_input("And how old is your mother? >\n")

#do not know how to deal with it, something is wrong.
result = add(your_age, your_mother_age)

print "That`s %r right?"%(result)    
