f = open('input3.txt')
m = []
index = 0
maxx = 0
minn = 10000000

for line in f:
    m.append(line.split())

for i in m:
    maxx = max(maxx, int(i[2]))
    minn = min(minn, int(i[2]))

for i in m:
    if int(i[2]) == maxx:
        d = open('oldest3.txt', 'w')
        d.write(str(i[0])+' '+str(i[1])+' '+str(i[2])
    if int(i[2]) == minn:
        d = open('youngest3.txt', 'w')
        d.write(str(i[0])+' '+str(i[1])+' '+str(i[2])
