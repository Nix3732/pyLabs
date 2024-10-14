s, cnt, sf, sd = str(input()), 1, [], ''
for i in range(0, len(s)-1):
    sd = s[i]
    if s[i] == s[i+1]:
        cnt += 1
    else:
        sf.append(sd)
        if cnt != 1:
            sf.append(cnt)
        print(cnt)
        cnt = 1
        sd = ''
sf.append(sd+s[-1])
if cnt != 1:
    sf.append(cnt)
print(*sf, sep='')



