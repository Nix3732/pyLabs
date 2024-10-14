s = 'G2y5'
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
c = 1
n = ''
f = []
final = []
for i in range(len(s)):
    if s[i] in numbers:
        n += s[i]
    else:
        if n == '':
            f.append(1)
        else:
            f.append(int(n))
        f.append(s[i])
        n = ''
if n == '':
    f.append(1)
else:
    f.append(int(n))

f = f[1:]

i = 0
while i != len(f):
    final.append(f[i]*f[i+1])
    i+=2
print(*final, sep='')