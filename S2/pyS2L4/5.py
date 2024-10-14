n = int(input())
d = {}
for i in range(n):
    buy = str(input()).split()
    ID = buy[0]

    if ID not in d:
        d[ID] = [(buy[1], buy[2])]
    else:
        d[ID].append((buy[1], buy[2]))

for key in d:
    for l in range(len(d[key])):
        print("id:", key, "Good:", d[key][l][0], "Value:", d[key][l][1])
