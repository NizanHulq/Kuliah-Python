
userWord = "belajar"
userWord = userWord.upper()#buat kapital
for letter in userWord:
	print(letter)


#latian lab yang for dgn string

kata=input()
print(kata)

print()
kata=input()
for huruf in kata:
    print(huruf)

print()
kata=input()
for huruf in kata:
    print(huruf,end="") #beda posisi mempengaruhi
    if huruf=="a":
        break

kata=input()
for huruf in kata:
    if(huruf!="a"):
        print(huruf,end="")

print()

for digit in input():
    if digit=="0":
        print("x", end="")
        continue