n = int(input())
data = input().split()

a = 0 # a buat insialisasi jumlah pertukaran Belum tau cara menghitung brp kali pertukaran
for k in range(n):
    posisiterkecil = k
    
    for i in range(k,n):
        if data[posisiterkecil] > data[i]:
            posisiterkecil = i
        
    # tukar
    a += 1
    temp = data[posisiterkecil]
    data[posisiterkecil] = data[k]
    data[k] = temp
    

print(data)
print(a)