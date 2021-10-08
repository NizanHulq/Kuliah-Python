#True or False # penulisannya harus benar
a=5<6
b=3>7
print(a,"mempunyai tipe",type(a))
print(b)
print(True>False) #yang di caplok jadi output


#coba
print()
a= 2
b = 3
c = 2.0
d = 3


x = a = b # (=) sama saja (==) 
y = a == b #kalo (= =) sama dengan pisah akan error
z = a == c
j = a == d
r = a < c
f = a > c
g = b <= d
h = d >= a
print(a,b,c,d,x,y,z,j,r,f,g,h,sep=' : ')

#coba lagi
print()
numberOfLions, numberOfLionesses = 5,6
answer = numberOfLions >= numberOfLionesses
print(answer)

print()
a,b,c,d = 1,2,3,4
r = a * b > c + d == d % b + a ** d  #masih bingung urutan operasi yang ini
print(r)

print()

#pake input
# latihan belum pake if
print("latihan belum pake if")
x=int(input()) > 100
print(x)

print()

#latihan pake if
print("latihan pake if")
n=int(input())
if(n>=80):
    print("lulus")

#latihan pake if dan else
print()
print("latihan pake if dan else")
n=int(input())
if(n>=80):
    print("lulus")
else:
    print("tidak lulus")

#if else bertingkat (nested if)
print()
print("if else bertingkat (nested if)")
nilai= int(input())
kehadiran= float(input())
if(nilai>=80):
    if(kehadiran>0.75):
        print("lulus")
    else:
        print("tidak lulus karena kehadiran kurang")
else:
    print("tidak lulus karena nilai")        

#the elif statement


print()
print("hari ini saya akan melakukan apa?")
print("masukkan hari", end=" : ")
hari_ini = str(input())

if(hari_ini == "Senin"):
    print("Saya akan kuliah")
elif(hari_ini == "Selasa"):
    print("Saya akan kuliah")
elif(hari_ini == "Rabu"):
    print("Saya akan kuliah")
elif(hari_ini == "Kamis"):
    print("Saya akan kuliah")
elif(hari_ini == "Jumat"):
    print("Saya akan kuliah")
elif(hari_ini == "Sabtu"):
    print("Saya akan kuliah")
elif(hari_ini == "Minggu"):
    print("Saya akan libur")
else:
    print("saya tidak melakukan apapun")


# latihan lagi
huruf = str(input("Jenis huruf apakah : "))
print('Jawabannya adalah', end=' ')
if(huruf=="a"):
    print('Huruf Vokal')
elif(huruf=="i"):
    print('Huruf Vokal')
elif(huruf=="u"):
    print('Huruf Vokal')
elif(huruf=="e"):
    print('Huruf Vokal')
elif(huruf=="o"):
    print('Huruf Vokal')
else:
    print('Huruf Konsonan')

#contoh lagi
    # read two numbers
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    # choose the larger number
    if number1 > number2:
        largerNumber = number1 #didalam if,else,elif bisa menggunakan variabel juga
    else:
        largerNumber = number2

    # print the result
    print("The larger number is:", largerNumber)

#percobaan


# read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
# we temporarily assume that the first number
# is the largest one
# we will verify it soon
largestNumber = number1
# we check if the second number is larger than current largestNumber
# and update largestNumber if needed
if number2 > largestNumber:
    largestNumber = number2
# we check if the third number is larger than current largestNumber
# and update largestNumber if needed
if number3 > largestNumber:
    largestNumber = number3
# print the result
print("The largest number is:", largestNumber)


#Fungsi max()
# read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

#
largestNumber = max(number1,number3,number2)
smallestNumber = min(number1,number3,number2)

# print the result
print("The largest number is:", largestNumber)
print("The smallest number is:",smallestNumber)
