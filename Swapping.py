c = open('countword.txt', 'r')
ct = c.read()
f = open('functionone.txt', 'r')
ft = f.read()
c2 = open('countword.txt', 'w')
f2 = open('functionone.txt', 'w')
c2.write(ft)
f2.write(ct)