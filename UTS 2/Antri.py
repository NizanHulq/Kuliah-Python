

Nsiswa = int(input())

DaftarNis = []
antrianSiswa = []


a = 0
while a != Nsiswa: 
    a+=1
    siswa = input().split()
    DaftarNis.append(siswa[0])
    antrianSiswa.append(siswa[1])

nis = input()
if nis == DaftarNis[0]:
    print("langsung bayar")
else:
    for i in range(DaftarNis.index(nis)-1,-1,-1):
        print(antrianSiswa[i])


