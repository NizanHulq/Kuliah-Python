x,y,z = [int(x) for x in input(). split()]
terbesar = max(x,y,z)
terkecil = min(x,y,z)
terbesar2 = x + y + z - terbesar - terkecil

print(terbesar2)

# cara 2 tidak work kalau ada variabel/input yang sama

print()

# if terkecil<x<terbesar :
#     print(x)
# elif terkecil<y<terbesar :
#     print(y)
# elif terkecil<z<terbesar :
#     print(z)