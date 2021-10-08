baris1 = input()
baris2 = input()

x = 0
for i in range(len(baris1)-1,-1,-1):
    if baris1[i] == baris2[i]:
        x = x+1
    else:
        break
print(x)