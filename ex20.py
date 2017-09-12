#if want use Chinese
#coding: utf-8
from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()
    
#'to commond readline change one by one. and as rewind appears, the next 'read' will be infuenced.' above this is my suspection  it`s not right hhh. the 'seek' can help you locate the file with out open it again.
#seek 函数是用来指定文件位置的函数
def rewind(f):
    f.seek(5,0)
    
#define how to print readline after line_count
def print_a_line(line_count, f):
    print line_count, f.readline()
    
#to fist open the file, or you`ll find it too much to type.
current_file = open(input_file)

#print
print "First let`s print the whole file:\n"

#use the FUNC to read whole file
print_all(current_file)

#only when you finished this script, you can know the meaning.
print "Now let`s rewind, kind of like a tape."

#it`s a very important step, it`s command seems to be to read down the file in ()
rewind(current_file)

#just print
print "Let`s print three lines:"

#if I open the file again, I can run this script successfully with out '.seek()', I think you can figure out the useway of 'seek'
#current_file = open(input_file)

#it dose`t mean which line you read. Just make your script printing beatiful.
current_line = 1
#print the 1st row.
print_a_line(current_line, current_file)

#print current_line
#add 1 to the crurrent line.
current_line = current_line + 1
#print the 2nd one.
print_a_line(current_line, current_file)

#print current_line
#to add 2 to the current_line. it`s quiet sample right?
current_line += 2
#print next row.
print_a_line(current_line, current_file)

#print_a_line(current_line,current_file)
#print current_line
