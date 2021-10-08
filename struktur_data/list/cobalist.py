makanan = " ayam, bakso, mie, nasi"

daftrmakan = makanan.split(', ')
print(daftrmakan)

# List vs String

daftrminum = ['jeruk', 'teh', 'lemon tea']

# jika ingin menggunakan if untuk list
if 'jeruk' in daftrminum:
    print('langsung pesan')
else:
    print('tidak jadi pesan')

# menggabungkan list
daftrmenu = daftrmakan+daftrminum
print(daftrmenu)