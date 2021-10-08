#cara nulis jum'at

kal = "hari jum'at"
kal3 = "Susi berkata, \"ayo kita main di hari jum'at\""
print(kal3)
print("hari\bjum'at") # menghapus karakter sebelumnya

print("""
 aku
    adalah
        saya
""")
# contoh fungsi
kalimat = kal.capitalize()

print('====')
print(kalimat)
print(kal[5])
print(kal[2:6])# dari karakter 2 sampai 5
print(kal[5:30])# tetap ada output sampai habisnya karakter
print(kal[-6:-2])

print('====')

kal = "senin saja"
kat1 = kal.upper()
kat2 = kal.lower()
kat3 = kal.replace("senin","sabtu")# didalam kurung adalah parameter
print(kat3)

print('====')
kat4 = kal.split()
print(kat4)
