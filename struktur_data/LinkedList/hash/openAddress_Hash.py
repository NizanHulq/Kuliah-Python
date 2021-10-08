h = int(input()) 
ls = [None]*h

data = list(map(int,input().split()))

for datum in data:
    key = datum%h
    if ls[key] == None:
        ls[key] = datum
        print(ls[key])
    else:
        cari = (key + 1)%h
        while ls[cari] != None:
            cari = (cari + 1)%h
        ls[cari] = datum
    
print(ls)