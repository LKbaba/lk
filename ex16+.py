from sys import argv

script, filename =argv

txt = open(filename)

#remember the '()' after read
print txt.read()

txt.close()
