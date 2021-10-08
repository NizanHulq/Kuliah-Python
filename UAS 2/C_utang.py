m = int(input())

data = []

for i in range(m):
    inp = list(map(int,input().split()))
    data.append(inp)

t = int(input())

total = 0
for utang in range(m):
    if t == data[utang][0]:
        total = total + data[utang][2]
print(total)

diUtang = 0
for utang in range(m):
    if t == data[utang][1]:
        diUtang = diUtang + data[utang][2]
print(diUtang)

bayar = []
for ngutang in range(m):
    if t == data[ngutang][0]:
        bayar.append(data[ngutang][1])

for i in sorted(bayar):
    print(i,end=" ")

