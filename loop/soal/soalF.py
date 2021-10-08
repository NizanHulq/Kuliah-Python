a,b,c,d,e = [int(a) for a in input().split()]
f = int(input())
if a >= f:
    a = 1
else:
    a = 0
if b >= f:
    b = 1
else:
    b = 0
if c >= f:
    c = 1
else:
    c = 0
if d >= f:
    d = 1
else:
    d = 0
if e >= f:
    e = 1
else:
    e = 0

lulus = a+b+c+d+e
print(lulus) 