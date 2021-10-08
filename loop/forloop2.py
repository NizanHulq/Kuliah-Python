
n = int(input())
for i in range(n) :
    print(i)


n = int(input())
for i in range(2,n) : # dimulai dari 2 sampai sejumlah 12 yang dimulai dari 0 tetapi 0,1 nya tidak ditulis ( sampai n-1 )
    print(i)


n = int(input())
for i in range(2,n,3) : # dimulai dari 2 sampai n-1 dengan selisih 3
    print(i)

# cari bilangan prima

n = int(input())
"""
dimulia  nya dari 0 trus di forloop i didalam range n+1(misal n=3 => 3+1 = 4)
trus didalam looping jika n mod i(i dimulai dari 0 truss lanjut looping satu persatu sampai sejumlah i)
trus jika sedang looping mod i ketemu nilai = 0 maka c ditambah 1
trus jika total c nya 2 maka bil. prima selain itu maka bukan bil. prima
"""
c=0
for i in range(n+1) :
    if n%(i+1)==0:
      c=c+1
if c==2:
    print(n,"adalah bilangan prima ")
else :
    print(n,"adalah bukan bilangan prima ")

# cara kedua
# tidak bisa bil 1 (ini carinya dengan menghilangkan looping angka 1 dan bilangan itu sendiri)

"""
n = int(input())
cek=True
for i in range(2,n) :
    if n%i==0:
        cek=False
        break
if cek==True:
    print(n,"adalah bilangan prima ")
else :
    print(n,"adalah bukan bilangan prima ")
"""

# cara ketiga

"""
n = int(input())
print("Bilangan Prima dari 1 sampai ",n," adalah : ")
for k in range (2,n+1)  :
    cek=True
    for i in range(2,k) :
        if k%i==0:
            cek=False
            break
        print(k)
    if cek==True:
"""

# latihan 1

"""
n,b = [int(n) for n in input().split()]

for i in range(1,n+1):
    if i%b == 0:
        print(i)
"""

# latihan 2

"""
a,b,c = [int(a) for a in input().split()]

for i in range(a,b+1):
    if i%c == 0:
        print(i)
"""

# latihan 3

"""
a,b = [int(a) for a in input().split()]

x = a+b

c=0
for i in range(x+1):
    if x%(i+1) == 0:
        c += 1
if c == 2 :
    print("prima")
else:
    print('bukan prima')
"""

# latihan 4

"""
n = int(input())

for i in range(n):
    i = '*'*n
    print(i)
"""

# latihan 5

"""
n = int(input())

for i in range(n):
    i = '*'* (i+1)
    print(i)
"""