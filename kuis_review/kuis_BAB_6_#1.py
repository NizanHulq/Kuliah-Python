n = int(input())
c=0
for i in range(n+1) :
    if n%(i+1)==0:
      c=c+1
if c==2:
    print("PRIMA")
else :
    print("BUKAN")