# def next_row(row):
#     row = [1] + row
#     for i in range(1, len(row) - 1):
#         row[i] += row[i + 1]
#     return row
#
#
# row = []
# n = int(input())
# for i in range(n):
#     row = next_row(row)
#     print((" "*n), *row)
#     n -= 1



def next_row(row):
    row = [1] + row
    for i in range(1, len(row) - 1):
        row[i] += row[i + 1]
    return row

row = []
n = (2**int(input())) - 1
print(' '*(n+1), '*')
for i in range(n):
    row = next_row(row)
    r = next_row(row)
    for j in range(len(r)):
        if r[j] % 2 == 1:
            r[j] = '*'
        else:
            r[j] = ' '
    print((' '*n), *r)
    n -= 1