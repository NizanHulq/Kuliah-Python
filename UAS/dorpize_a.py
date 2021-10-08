nama = input().split()

x = []
for i in nama:
    a = 0
    for j in i :
        if j == 'a':
            a += 1
    x.append(a)

terbesar = max(x)

for i in nama:
    a = 0
    for j in i :
        if j == 'a':
            a += 1
    if a == terbesar:
        print(i)
        break
