# soal 1
"""a = input()

b= ord(a)

if  65 <= b <= 90 :
    print('kapital')
else:
    print('bukan')"""

# soal 2
"""kata = input()
a = 0
for i in kata :
    if ord(i) in range(65,91):
        a += 1
print(a)"""

#soal 3
kataacak = input()
kecil = kataacak[1:].lower()
depan = kataacak[0].upper()
print(depan+kecil)


    