# void function dan fruitful function
# void function merpakan fungsi yang tidak bernilai seperti fungsi salam()
# fruitful function mrpakan fungsi bernilai seperti len() / fungsi yg bisa dimasukkan ke variabel

# contoh
"""def salam(waktu): 
    print("Selamat", waktu, "!!")

x = salam("pagi") # salam tidak bisa dijadikan sebagai isi dari variabel
y = len("pagi") # jika di print outputnya adalah 4

print(x)
print(y)"""

# membuat fruitful function
"""
import math
def vol_tabung(r, t):
    volume = math.pi * r * r * t
    return volume
    
hasil = vol_tabung(7, 9)
print(hasil)
"""
import math
def area_circle(r):
    return math.pi * r * r

def vol_tabung(r, t):
    return area_circle(r) * t

def vol_int(r, t):
    return int(vol_tabung(r, t))

hasil_int = vol_tabung(7, 9)
print(hasil_int)

