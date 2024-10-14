f = open('input2.txt')
m = []

for line in f:
    m.append(int(line))

m.sort()
d = open('output2.txt', 'w')
for i in m:
    d.write(str(i))
    d.write('\n')
