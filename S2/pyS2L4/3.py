city_main = set()
n = int(input())
i = 0
city_local = input()
letter = city_local[-1]
city_main.add(city_local)
print("OK")
while i < n-1:
    city_local = input()
    if (city_local in city_main) or (city_local[0] != letter):
        print("REPEAT")
        i -= 1
    else:
        print("OK")
        city_main.add(city_local)
        letter = city_local[-1]
    i += 1
