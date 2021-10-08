# list biasa
numbers = [10,21,42,63,84]
print(numbers[0])
print(numbers[-5])

print()
#mengganti list
numbers = [10,21,42,63,84]
numbers[2] = 52
print(numbers[-3])

print()
#menyamakan list
numbers = [10,21,42,63,84]
numbers[2] = numbers[4]
print(numbers)

print()
# fungsi len [The len()function]
numbers = [10,21,42,63,84]
l = len(numbers)
print(l)

print()
# menghapus element dari list
numbers = [10,21,42,63,84]
l = len(numbers)

del numbers[0]

print(l)
print(numbers)
print(numbers[0])

print()
#menambahkan elemenet kedalam list [ append() and insert()] 
numbers = [10,21,42,63,84]
l = len(numbers)
print(l)

# append() + at the and [list.append(value)]
numbers.append(11) # namanya method
print(numbers)
# insert() + at any place [list.insert(location,value)]
numbers.insert(0,22)
print(numbers)

print()
numbers = []
numbers.insert(3,22)
print(numbers)

# di dalam list ada list atau list multidimensi
print()
mylist = [1,[1,2],["apa", 32 , [0,1]] ]
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[2][2]) #element ke 2 dari mylist diambil element ke 2 nya
print(len(mylist))
print(len(mylist[2]))

print()
mylist = [[0,1],[1,2],["apa", 32 , [0,1]] ]
for i in mylist:
    print(i)
    for j in i :
        print(j) 

print()
mylist = [[[1]*3]*3]*3
print(mylist)
print()
for i in mylist:
    print(i)

print()
mylist = [[0,1],[1,2],["apa", 32 , [0,1]] ]

s = mylist[0:2] # dari 0 sampai sebelum 2
s = mylist[1:] # ini maksudnya dimulai dari list ke 1 sampai seterusnya
print(s)