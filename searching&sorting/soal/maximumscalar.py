n = int(input())
x = input().split()
y = input().split()

jumlah = 0
for i in range(n):
    a = int(x[i])*int(y[i])
    jumlah = a + jumlah

print(jumlah)
