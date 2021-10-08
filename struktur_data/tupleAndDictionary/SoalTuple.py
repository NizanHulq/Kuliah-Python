

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", "R&B", "progressive rock", "disco") 
print(genres_tuple)

# nomor 1 mencari panjang tuple

print(len(genres_tuple))

# nomor 2 menampilkan elemen index ketiga

print(genres_tuple[3])

# nomor 3 menggunakan slicing untuk index 3,4,5

print(genres_tuple[3:6])

# nomor 4 mencari 2 elemen pertama dari tuple

print(genres_tuple[ :2])

# nomor 5 mencari index pertama dari disco

print(genres_tuple.index("disco"))

# nomor 6 membuat sorted list

c_tuple=(-5,1,-3)

print(sorted(c_tuple))