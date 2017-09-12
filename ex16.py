from sys import argv

script, filename =argv

print "We`re going to erase %r."%filename
print "If you don`t want that, hit CTRL-C(^C)."
print "If you do want taht, hit RETURN."

raw_input("?")

print "Opening the file..."
#we should add 'w' cause 'open' do not have the right to insert strings without it.
target = open(filename, 'w')

print "Truancating the file. Goodbye!"
#to clean the file, and you don`t need such a step due to the 'w' above.
#target.truncate()

print "Now I`m going to aks you for three lines."

line1 = raw_input("line 1: ")   
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I`m going to write these to the file."

#this is really hard hahaha. and you mast add the % before the ')'. 
target.write("%s\n%s\n%s"%(line1, line2, line3))
#target.write("\n")

#if you type "line", the result will display the actually line2 instead of what you input just above.
#target.write(line2)

#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally, we close it."
target.close()
