#invoke the function. to use 'raw_input' only.
#from sys import argv

#match up to the FUNC. to use 'raw_input' only.
#script, filename = argv

#this is an order. explain the 'txt', and command it to open a file. to use 'raw_input' only. and the 'filename' must be input, can`t append it directly.
#filename = raw_input("> ") 
filename = ("ex15_sample.txt")
txt = open(filename)

#show the filename to user
print "Here`s your file %r:"%filename
#like an order. let the txt read itself and print it later.
print txt.read()

#just make the use know what to do next.
print "Type the filename again:"
#to let user input what`s the 'file_again' is. and add a '> ' in front of it.
file_again = ("ex15_sample.txt ")

#in order to tell the next print what to print.
txt_again = open(file_again)

#to print the txt_again.
print txt_again.read()

print "Anymore?"
file_add =("ex15+.txt")
txt_add = open(file_add)
#'readline can only read the first raw of txt, and I shoule know more about it.
print txt_add.readline()
print txt_add.readline()
#when you finished, remember to close the 'txt', that`s a improtant spirit of programing. but I don`t know whether we should print it or not.
print txt.close()
txt_again.close()
