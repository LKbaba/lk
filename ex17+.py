from sys import argv

script, txt_1, txt_2 =argv

one = open(txt_1).read()
two = open(txt_2, 'w')
two.write(one)
