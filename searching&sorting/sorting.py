
# code algoritma sorting masih kacau blum bisa digunakan selain list dibawah
# Bubble Sort
print('===bubble sort===')
list_a = [5, 4, 2, 1, 3]
length = len(list_a)
iterasi = 0
for i in range(length-1):
    iterasi+=1 # cek berapa kali di tukar urutannya
    for j in range(length-1):
        if list_a[j] > list_a[j+1]:
            tmp = list_a[j]
            list_a[j] = list_a[j+1]
            list_a[j+1] = tmp
    print(iterasi,list_a) # cek langkah pertukaran
print('hasil',list_a)

# Selection Sort
print('===selection sort===')
list_a = [5, 4, 2, 1, 3]
length = len(list_a)
for i in range(length-1):
    smallest = i
    for j in range(i+1, length):
        if list_a[j] < list_a[smallest]:
            smallest = j
    tmp = list_a[smallest]
    list_a[smallest] = list_a[i]
    list_a[i] = tmp
print(list_a)

# Merge Sort
print('===merge sort===')
def ms(list):
 print('Memecah List', list)
 n = len(list)
 if n < 2:
     return list
 else:
     mid=n//2
     left=list[:mid]
     right=list[mid:]
     ms(left)
     ms(right)
     i=0
     j=0
     k=0
     while i < len (left) and j < len (right):
         if left[i]<right[j]:
             list[k]=left[i]
             i=i+1
         else:
             list[k]=right[j]
             j=j+1
         k=k+1
     while i < len (left):
         list[k]=left[i]
         i=i+1
         k=k+1
     while j < len (right):
         list[k]=right[j]
         j=j+1
         k=k+1
 print('menggabungkan list ',list)  
list = [5, 4, 2, 1, 3]
ms(list)


# insertion sort
print('==insertion==')
def InsertionSort(val):
   for index in range(1,len(val)):
 
     valueaktif = val[index]
     posisi = index
 
     while posisi>0 and val[posisi-1]>valueaktif:
         val[posisi]=val[posisi-1]
         posisi = posisi-1
 
     val[posisi]=valueaktif
 
DaftarAngka = [23,7,32,99,4,15,11,20]
InsertionSort(DaftarAngka)
print(DaftarAngka)



# fungsi dari python sorted
print('===sorted===')
list_a = [5, 4, 2, 1, 3]
urut = sorted(list_a)

print(urut)

# urutin huruf
'===urutin huruf==='
list_a = ['b', 'd', 'a', 'f', 'k']

angka = []
for a in list_a:
    asci = ord(a)
    angka.append(asci)

length = len(angka)
for i in range(length-1):
    for j in range(length-1):
        if angka[j] > angka[j+1]:
            angka[j],angka[j+1] = angka[j+1],angka[j]

huruf = []
for b in angka:
    hrf = chr(b)
    huruf.append(hrf)

print(huruf)