m = str(input())
to_del = '-_,.*!?:;"()'
for x in to_del:
    m = m.replace(x, '')
data = {}
c = 0
m = m.lower().split()
for i in m:
    if i not in data:
        data[i] = [c, 1]
        c += 1
    else:
        data[i][1] += 1

answer = []
for i in data:
    answer.append([i, data[i][1]])

for i in range(len(answer)):
    for j in range(i + 1, len(answer)):
        if answer[i][1] < answer[j][1]:
            tmp = answer[i]
            answer[i] = answer[j]
            answer[j] = tmp
        elif answer[i][1] == answer[j][1]:
            if answer[i][0] > answer[j][0]:
                tmp = answer[i]
                answer[i] = answer[j]
                answer[j] = tmp

for i in range(len(answer)):
    print(answer[i][0], '(' + str(answer[i][1]) + ')')
