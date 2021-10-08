x = int(input())
y = input().split()
z = list(map(int,y))

a = 0
bc = 0
ab = 0
b = 0
for i in range(x):
    if z[i] >= 75:
        a += 1
    elif z[i] <= 45:
        bc += 1
    elif z[i] > sum(z)//x :
            ab += 1
    else:
        b += 1

print(a,ab,b,bc)
