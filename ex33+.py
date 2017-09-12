def ok(a, b):
    return a + b
print "What are the two favorite numbers?"
a = input("> ")
b = input('> ')

O = ok(a, b)

while O < 10:
    print O
    O += a
print "the number will be counted to 9, right?"
