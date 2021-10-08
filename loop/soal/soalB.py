a, b = [int(a) for a in input().split()]
c, d = [int(c) for c in input().split()]
e, f = [int(e) for e in input().split()]
g, h = [int(g) for g in input().split()]
atas1 = a * e + b * g
atas2 = a * f + b * h
bawah1 = c * e + d * g
bawah2 = c * f + d * h
print(atas1, atas2)
print(bawah1, bawah2)