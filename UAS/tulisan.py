inp = input()

kecil = inp.lower()
list1 = kecil.split()


list2 = [list1[0]]
for i in list1[1:]:
    kecil = i.lower()
    kapital = kecil[0].upper()
    kecil2 = kecil[1:]
    camel = kapital + kecil2
    list2.append(camel)


camelcase = "".join(list2)

print(camelcase)




    