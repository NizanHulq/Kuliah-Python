tahun = int(input())


if tahun%400 == 0:
    print('kabisat')
elif tahun%100 == 0:
    print('kabisat')
elif tahun%4 == 0:
        print('kabisat')
else:
    print('Bukan kabisat')