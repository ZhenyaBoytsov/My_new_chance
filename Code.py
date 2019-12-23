f1 = open('Main.txt', 'r')
f2 = open('doc1.txt', 'w')
f3 = open('doc2.txt', 'w')

i = 0
for line in f1:
    i = 1 - i
    if(i): f2.write(line)
    else: f3.write(line)

f1.close()
f2.close()
f3.close()
