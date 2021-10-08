n = int(input())

push = input().split() 

hasil = []


index = 0
for i in range(n):
    if hasil == []:
        hasil.append(push[i])
    elif len(hasil)%2 != 0:
        hasil.insert(index,push[i])
        index += 1
    elif len(hasil)%2 == 0:
        hasil.insert(i//2,push[i])

print(" ".join(hasil))
