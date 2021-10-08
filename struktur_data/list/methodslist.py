# fungsi .append()
hewan = [ 'ayam','burung','bebek']
hewan.append('ular')
print(hewan)



# fungsi .extend()
hewan1 = [ 'ayam','burung','bebek']
hewan2 = ['buaya','biawak','komodo']
hewan1.extend(hewan2)
print (hewan1)

# fungsi .insert()
hewan = [ 'ayam','burung','bebek']
hewan.insert(1,'singa')
print(hewan)

# fungsi sort()

angka = [1,34,43,12,11,23,56]
angka.sort()
print(angka)

kata = ['makan','ayam','goreng']
kata.sort()
print(kata)

# fungsi .reverse()

angka1 = [1,2,3,4,5,6,7,8,9]
angka1.reverse()
print(angka1)

# fungsi .clear()
angka = [1,34,43,12,11,23,56]
angka.clear()
print(angka)

# fungsi .copy() (masih belum tau implementasi kegunaan copy())
angka = [1,34,43,12,11,23,56]
angka1 = angka.copy()
print(angka)
print(angka1)

# fungsi .count()
angka = [1,1,1,2,2,2,2,3,3]
jumlh_1 = angka.count(1)
jumlh_2 = angka.count(2)
jumlh_3 = angka.count(3)

print(jumlh_1)
print(jumlh_2)
print(jumlh_3)

# fungsi .index()
angka = [1,1,1,2,2,2,2,3,3]
idx = angka.index(2)
print(idx)

# fungsi .remove()
angka = [1,34,43,12,11,23,56]
angka.remove(1)

print(angka)

# fungsi .pop()

angka = [1,34,43,12,11,23,56]
angka1 = angka.pop(3)
print(angka)
print(angka1)
angka.




