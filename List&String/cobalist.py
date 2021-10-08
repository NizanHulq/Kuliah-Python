# coba apakah bisa semua tipe data
mylist = [1, None, True, 'I am a string', 256,0]
print(mylist)

# coba apa hasilnya

mylist = [1,2,3,4,5]

mylist[0],mylist[4] = mylist[4],mylist[0]
print(mylist)
mylist[1],mylist[3] = mylist[4],mylist[0]
print(mylist)

print()
mylist = [1,2,3,4,5]

mylist[0] = mylist[4]
mylist[4] = mylist[0]
print(mylist)