# operasi + (kalo + hanya string dgn string)
a = "aku"
d = "dia"
s = a + d # tidak bisa string + integer 
print(s)

# operasi * ( hanya bisa string dengan integer)
a = "aku"
d = "dia"
s = a * 3
print(s)

# operasi ASCII

#untuk mencari kode ascii dari string
huruf = 'a'
print(ord(huruf))
huruf = 'A'
print(ord(huruf))
huruf = 'b'
print(ord(huruf))
huruf = ' '
print(ord(huruf))

#untuk mencari string dari kode ascii
kode = 77
print(chr(kode))
kode = 33
print(chr(kode))

#split [untuk membuat string menjadi list]
s = "saya makan sate kambing"
s1 = s.split()
print(s1)
"""
s = input()
s1 = s.split()
print(s1)
"""
# join [untuk membuat list menjadi string]
s = ["saya", "makan", "sate", "kambing"]
s1 = "--"
s2 = s1.join(s)
print(s2)
print()
s = ["saya", "makan", "sate", "kambing"]

s2 = " ".join(s)
print(s2)

print()
# string immutable ( string tidak bisa di ubah)
s = "saya makan kambing"
list_s = s.split()
list_s[0] = "kamu"
list_s.insert(2,'sate')
s = " ".join(list_s)
print(s)