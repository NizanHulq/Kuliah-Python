t = (123 , 341, 'Hai')

print(t)

t = 1234, 432, 'World!'
print(t)

kosong = ()

satu = ('satu',)
print(satu)


# membuat tuple
nama = ('apa', 'kode', 'saya')

# mengakses nilai tuple
print(nama[1])

t = (123 , 341, 'Hai','apa', 'kode', 'saya')
print(t[1:4])


nama = ('apa', 'kode', 'saya')
t = (123 , 341, 'Hai')

gabung = nama + t
print(gabung)
print(len(gabung))

# sorting tuple

tup = (1,4,6,2,4,3,8,7)
print(sorted(tup))
print(tuple(sorted(tup)))

# nested tuple

my_tup = ("hello", [1, 2, 3], (4, 5, 6),True,('hai','kamu')) 
print(my_tup)
print(my_tup[1][2])
print(my_tup[2][0:2])

# perbedaan tuple list

listBilangan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tupleBilangan = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)