x,y,z = [int(x) for x in input().split()]
terbesar1 = max(x,y,z)
terkecil = min(x,y,z) # coba pake if else dari min max nya buat ngitungnya

jumlah = x + y + z - terkecil

print(jumlah)
