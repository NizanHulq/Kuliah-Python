susi = input().split()
santi = input().split()

h,b,t = susi[0],susi[1],susi[2]
h2,b2,t2 = santi[0],santi[1],santi[2]

if t == t2:
    if b == b2:
        if h == h2:
            print('Kembar')
        elif b < b2:
            print('Susi')
        else:
            print('Santi')
    elif b < b2:
        print('Susi')
    else:
        print('Santi')
elif t < t2:
    print('Susi') 
else:
    print('Santi')   
