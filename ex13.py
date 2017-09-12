from sys import argv

script, first, second, third, fouth = argv
print "What do you like?"
apple = raw_input()
evil = raw_input("What do you hate?")
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "You well get:", fouth
print "You like %s."%apple
print "What do you hate?%r."%evil
