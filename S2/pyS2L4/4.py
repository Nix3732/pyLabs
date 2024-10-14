string = "one   two one one three"
s = string.split(' ')
m = []
r = []
data = {}

for i in range(len(s)):
    if s[i] != '':
        m.append(s[i])

for i in m:
    data[i] = data.get(i, 1) + 1
    r.append(data[i]-2)
print(*r)
print(*m)