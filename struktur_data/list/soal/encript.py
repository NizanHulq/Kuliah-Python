baris1 = list(map(int,input().split()))
baris2 = list(map(int,input().split()))

a = []
for i in baris2 :
    a.append(chr(i + 64))
print(''.join(a))
