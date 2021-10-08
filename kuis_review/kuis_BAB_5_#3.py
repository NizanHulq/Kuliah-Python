# masih kurang tahun kabisat
tanggal = input().split()
hari = int(tanggal[0])
bulan =int(tanggal[1])
tahun =int(tanggal[2])

# if bulan == [2,4,6,9,11] : 
#     if hari in range(1,31):
#         print("valid")
#     else:
#         print("tidak valid")
# elif bulan == [1,3,5,7,8,10,12] :
#     if hari in range(1,32):
#         print("valid")
#     else:
#         print("tidak valid")
# else:
#     print("tidak valid")

if tahun%4 == 0:
    if bulan == 2 : 
        if hari in range(1,30):
            print("valid")
        else:
            print("tidak valid")
elif tahun%100 == 0:
    if bulan == 2 : 
        if hari in range(1,30):
            print("valid")
        else:
            print("tidak valid")
elif tahun%400 == 0:
    if bulan == 2 : 
        if hari in range(1,30):
            print("valid")
        else:
            print("tidak valid")
elif tahun > 0 :
    if bulan == 2 : 
        if hari in range(1,29):
            print("valid")
        else:
            print("tidak valid")
    elif bulan == 4 : 
        if hari in range(1,31):
            print("valid")
        else:
            print("tidak valid")
    elif bulan == 6 : 
        if hari in range(1,31):
            print("valid")
        else:
            print("tidak valid")
    elif bulan == 9 : 
        if hari in range(1,31):
            print("valid")
        else:
            print("tidak valid")
    elif bulan == 11 : 
        if hari in range(1,31):
            print("valid")
        else:
            print("tidak valid")
    elif bulan == 1 : 
        if hari in range(1,32):
            print("valid")
        else:
            print("tidak valid")
    elif bulan == 3 : 
        if hari in range(1,32):
            print("valid")
        else:
            print("tidak valid")
    elif bulan == 5 : 
        if hari in range(1,32):
            print("valid")
        else:
            print("tidak valid")
    elif bulan == 7 : 
        if hari in range(1,32):
            print("valid")
        else:
            print("tidak valid")
    elif bulan == 8 : 
        if hari in range(1,32):
            print("valid")
        else:
            print("tidak valid")
    elif bulan == 10 : 
        if hari in range(1,32):
            print("valid")
        else:
            print("tidak valid")
    elif bulan == 12 : 
        if hari in range(1,32):
            print("valid")
        else:
            print("tidak valid")
    else:
        print("tidak valid")
else:
    print("tidak valid")