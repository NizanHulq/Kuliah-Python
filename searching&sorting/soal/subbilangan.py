n = int(input())
list_a = input().split()
masuk = input().split()
x = int(masuk[0])
y = int(masuk[1])
z = masuk[2]

for i in range(n):
    posisi = i
    for j in range(i,n):
        if z == "D" :
            if list_a[posisi] < list_a[j]:
                posisi = j
        if z == "A" :
            if list_a[posisi] > list_a[j]:
                posisi = j
    tmp = list_a[posisi]
    list_a[posisi] = list_a[i]
    list_a[i] = tmp

out = list_a[x-1:y]
print(out)
