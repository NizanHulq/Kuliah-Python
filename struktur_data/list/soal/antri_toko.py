inp = input()
list_inp = inp.split()

p = 0
l = 0
for i in list_inp:
    if i == 'P':
        p += 1
    elif i == 'L':
        l += 1

if p > l :
    print('aktif')
else:
    print('tidak aktif')