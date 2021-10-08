gen0 = input()
gen1 = input()
penanda = input()

a = []
for i in gen0:
    a.append(i)
b = []
for i in gen1:
    b.append(i)
c = []
for i in penanda:
    c.append(i)

hasil = []
for i in range(len(c)):
    if c[i] == '0':
        c[i] = a[i]
    else:
        c[i] = b[i]
   
print("".join(c))