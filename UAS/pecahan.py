a,b,c,d = [int(a) for a in input().split()]

def hitung_FPB(x, y):
   # pake algoritma Euclidean
   while(y):
       x, y = y, x % y
   return x

e = a*d + b*c
f = b*d

def fpb():
    if e > f:
        return hitung_FPB(e,f)
    else:
        return hitung_FPB(f,e)

e2 = e//fpb()
f2 = f//fpb()

print(e2,f2)
