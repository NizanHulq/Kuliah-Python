# pemanggilan fungsi
"""
import math

x = int(input())
hasilakar = math.sqrt(x)
print(hasilakar)
"""

# membuat fungsi sederhana
"""
def salam():
    print ("Selamat Pagi")

print("ini awall")
salam()
print("ini akhir")
"""

# Parameter fungsi

def salam(waktu): # waktu adalah parameternya / variabel yang nanti buat input di dalam fungsi
    print("Selamat", waktu, "!!")

salam(8)
salam("Siang")
salam("Sore")

print()
# dengan 2 parameter atau lebih

def cek_huruf(huruf, s):
    ada = False
    for i in s:
        if huruf == i:
            ada = True
    if ada:
        print("Huruf ditemukan")
    else:
        print("Huruf tidak ada")

cek_huruf("k", "pakaian")

"""
def prima_bukan(n):
    c=0
    for i in range(n+1) :
        if n%(i+1)==0:
          c=c+1
    if c==2:
        print(n,"adalah bilangan prima ")
    else :
        print(n,"adalah bukan bilangan prima ")

prima_bukan(int(input()))
"""


