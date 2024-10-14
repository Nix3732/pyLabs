m = [[], [], []]
for x in range(3):
    for y in range(3):
        m[x].append(int(input()))

if (m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[0][2] * m[1][0] * m[2][1]
    - m[0][2] * m[1][1] * m[2][0] - m[0][1] * m[1][0] * m[2][2] - m[0][0] * m[1][2] * m[2][1]) != 0:
    print("Линейно независимы")
else:
    print("Линейно зависимы")

for x in range(3):
    for y in range(3):
        print(m[x][y], end=' ')
    print('')
