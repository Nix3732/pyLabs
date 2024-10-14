print('Введите строку:')
s = str(input())
s = s.split(' ')
final = ''
for i in range(len(s)):
    final += s[i][0]
final = final.upper()
print(final)