# rekursi atau perulangan
""" n = 4 maka jika n = 1 return nilai = 1 tetapi tidak maka fact(n) terdefinisikan n*fact(n-1) berarti 4 * fact(3) 
(fact(3) terdefinisikan 3 * fact(2) (fact(2) terdefinisikan 2 * fact(1) (fact(1) sudah masuk syarat if = 1 
maka return atau terdefinisikan sebagai 1))) maka fact(4) akan menghasilkan return 4 * 3 * 2 * 1  """
"""
def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)
print(fact(4)) 
"""
# Praktik

def luas_segitiga(alas,tinggi):
    return alas * tinggi / 2

def luas_trapesium(atas,bawah,tinggi):
    return (atas + bawah) * tinggi / 2

def mulai():
    print("Pilih menu berikut :")
    print("[1] Luas Segitiga")
    print("[2] Luas Trapesium")
    
    inp = int(input())

    if inp == 1:
        print("Inputkan alas dan tinggi :")
        a = int(input("Alas : "))
        t = int(input("Tinggi : "))
        print(luas_segitiga(a,t))
    elif inp == 2:
        print("Inputkan 2 sisi sejajar dan tinggi")
        a = int(input("Sisi atas : "))
        b = int(input("Sisi bawah : "))
        t = int(input("Tinggi : "))
        print(luas_trapesium(a,b,t))
    else:
        print("Input anda mungkin tidak sesuai perintah!! ")

print("Memulai program...")
mulai()
print("Mengakhiri program...")

