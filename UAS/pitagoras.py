a,b,c = [int(a) for a in input().split()]
# masih belum bener
 
if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print('pitagoras')
else:
    print('bukan') 
