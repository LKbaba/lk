from sys import argv

script, user_name, mood =argv
prompt = "please anwser me "

print "Hi %s, I`m the %s script."%(user_name, script)
print "I`d like to ask you a few questions."
print "Do you like me %s?"%user_name
likes = raw_input(prompt)

print "Where do you live %s?"%user_name
lives = raw_input(prompt)

print "Seems that you are %r?"%mood
attitude = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
And suprisingly, you are very %s!
"""%(likes, lives, computer, mood)
