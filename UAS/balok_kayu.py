msk = input().split()
balok = list(map(int, msk))

length = len(balok)

for i in range(length-1):
    for j in range(length-1):
        if balok[j] > balok[j+1]:
            balok[j+1],balok[j] = balok[j],balok[j+1]

ubah = list(map(str, balok))
gabung = " ".join(ubah)
print(gabung)