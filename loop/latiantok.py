"""
for i in range(1, 10): 
	if i % 2 == 0: 
		print(i)
"""

text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

print()





text = "pyxpyxpyx" 
for letter in text: 
    if letter == "x": 
        continue 
    print(letter, end="")
print()
print()

for i in range(3): 
	print(i, end=" ")

print()

for i in range(6, 1, -2): # 6 awal 1 batas akhir -2 selisih nya
	print(i, end=" ")

print()
print()

n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

i = 1
while i < 5:
    print(i)
    i += 1 # +1 adalah selisih
else:
    print("else:", i)
    
print()
print()
i = 111 
for i in range(2, 1): 
	print(i) 
else: 
	print("else:", i)

print()

n = range(4)
for num in n:
    print(num -2)
else:
    print(num)