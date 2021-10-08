msk = list(map(int,input().split()))
a = int(input())

b = -1 
for i in msk:
    if i < a:
        b += 1
print(b)

c = 0
for j in msk:
    if j > a:
        c += 1
print(c)