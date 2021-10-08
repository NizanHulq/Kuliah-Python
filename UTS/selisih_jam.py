a,b,c = [int(a) for a in input().split()]
p,q,r = [int(p) for p in input().split()]

baris1 = a*3600 + b*60 + c
baris2 = p*3600 + q*60 + r
if baris1 < baris2:
    selisih = int(baris2 - baris1)
elif baris1 > baris2:
    selisih = int(baris1 - baris2)

jam = selisih//3600
menit = (selisih%3600)//60
detik = selisih%3600%60
print(jam,menit,detik)
