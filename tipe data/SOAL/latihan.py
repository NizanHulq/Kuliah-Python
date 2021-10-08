#latihan variable
john = 3
mary = 5
adam = 6
print(john,mary,adam, sep=',')

print("john : ",john,",","mary : ",mary,",","adam : ",adam)


totalApples = john+mary+adam
print(totalApples)
print("jumlah total apel : ",totalApples)

#coba
print()
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.60934
kilometers_to_miles = kilometers/1.60934

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

print()

#latihan boolean

penghasilan = int(input("Masukkan penghasilan anda :"))

if penghasilan <= 50e6 :
    pajak = 5/100
elif 50e6 < penghasilan <= 250e6 :
    pajak = 15/100
elif 250e6 < penghasilan <= 500e6 :
    pajak = 25/100
elif penghasilan > 500e6 :
    pajak = 30/100

p = round(pajak,2)
q = int(penghasilan * pajak)
print("Persen pajak adalah",p,"dan total pajak yang harus dibayar senilai",q)
