tahun = int(input())


if tahun%4 == 0:
    print('kabisat')
elif tahun%100 == 0:
    print('kabisat')
elif tahun%400 == 0:
        print('kabisat')
else:
    print('bukan kabisat')
