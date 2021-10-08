nama = input().split()

a = []
for i in range(len(nama)):
    pjg = len(nama[i])
    a.append(pjg)

terkecil = min(a)

for i in nama:
    while len(i) == terkecil:
        print(i)
        break
    



