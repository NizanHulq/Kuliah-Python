n = int(input())
resep = list(map(int,input().split()))
stok = list(map(int,input().split()))

a = 0
for i in range(n):
    if resep[i] <= stok[i]:
        a += 1

if a == n:
    print('YA')
else:
    print('TIDAK')