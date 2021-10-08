cari = int(input())
data = [4,31,44,83,94,144,200,247,250,299]

depan = 0
belakang = 9
tengah = (depan+belakang)//2
while data[tengah] != cari:
    tengah = (depan+belakang)//2
    if data[tengah] == cari:
        print("Ketemu")
    elif data[tengah] < cari:
        depan = tengah
    elif data[tengah] > cari:
        belakang = tengah

    
    


