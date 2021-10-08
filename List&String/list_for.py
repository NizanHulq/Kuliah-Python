#menambahkan isi list otomatis menggunakan for
numbers = [] # inisialisasi list

for i in range(100):
    numbers.append(i)
print(numbers)
print()
numbers = [] 
for i in range(100):
    numbers.append(i+1)
print(numbers)
print()
numbers = [] 
for i in range(100):
    numbers.append(0)
print(numbers)

print()
numbers = [0] * 10
print(numbers)
"""
print()
numbers = [] 
for i in range(3):
    numbers.append(int(input()))
print(numbers)

print()
numbers = []
x = int(input())
for i in range(100):
    numbers.append(x)
print(numbers)
"""
# list for coba
mylist = [1, None, True, 'I am a string', 256,0]

for i in mylist:
    print(i)
print('==ini sama==')

for i in range(len(mylist)):
    print (mylist[i])

print()
for i in range(len(mylist)):
    print (i)
    

