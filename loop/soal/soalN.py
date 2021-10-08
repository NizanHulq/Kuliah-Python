a = int(input())
if a > 1:
    for i in range(2,a):
        if (a % i) == 0:
            print("BUKAN")
            break
    else:
        print("PRIMA")

else:
    print("BUKAN")