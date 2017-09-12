#i = 0
numbers = []
print "Please give me two numbers both are under 10."

#there can`t be raw_input, I don`t know why. And you can directly input.
#O = input() 
K = input()
i = input()
#numbers = range(0,4) 

while i < 15:
    print "At the top i is %d"%i
    numbers.append(i)
    i += K
    print "Numbers now: ", numbers
    print "At the bottom i is %d"%i

print "The numbers: "

for num in numbers:
    print num
