f = open('input1.txt')

for line in f:
    num = line.split()

counter = 1
for i in num:
    counter *= int(i)

d = open('output1.txt', 'w')
d.write(str(counter))
