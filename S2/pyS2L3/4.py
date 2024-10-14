m = str(input()).split()
data = {}
c = 0
for i in m:
    if i not in data:
        data[i] = [c, 1]
        c+=1
    else:
        data[i][1] += 1
answer = []
for i in data:
    answer.append(data[i][1])
print(*answer)
