list_a = [3, 5, 2, 5, 7, 8, 1, 0, 4, 14, 3, 5, 
12, 5, 9, 8, 11, 10, 5, 1,13, 1, 8, 5, 7, 2, 1, 0, 0, 41]

length = len(list_a)
for i in range(length-1):
    for j in range(length-1):
        if list_a[j] > list_a[j+1]:
            tmp = list_a[j]
            list_a[j] = list_a[j+1]
            list_a[j+1] = tmp
print(list_a)

def cari_binary(list_a, l, r, nilai):
    idtengah = (l + r) // 2
    if nilai == list_a[idtengah]:
        return idtengah
    elif l > r:
        return -1
    elif nilai > list_a[idtengah]:
        return cari_binary(list_a, idtengah+1, r, nilai)
    elif nilai < list_a[idtengah]:
        return cari_binary(list_a, l, idtengah-1, nilai)
n = 12
indeks = cari_binary(list_a, 0, len(list_a)-1, n)
if indeks != -1:
    print(n, "ditemukan di indeks", indeks)
else:
    print(n, "tidak ditemukan")