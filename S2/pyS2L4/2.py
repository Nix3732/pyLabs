print("Первое множество")
a = {int(input()) for i in range(int(input()))}
print("Второе множество")
b = {int(input()) for j in range(int(input()))}

if (len(a.intersection(b)) == min(len(a), len(b))
        and len(a.intersection(b)) != max(len(a), len(b))):
    print("true")
else:
    print("false")