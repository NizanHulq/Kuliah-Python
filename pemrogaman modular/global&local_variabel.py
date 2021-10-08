# local variabel
"""def fungsi_satu(n): # fungsi_satu adalah local variabel karena x hanya ada di fungsi_satu
    x = 5
    return n+x
def fungsi_dua(n):
    return n+x # akan eror pada x nya karena tidak di definisikan di fungsi_dua

print(fungsi_satu(5))
print(fungsi_dua(5))""" # syntax akan eror karena x tidak di definisikan di fungsi_dua

# global variabel
def fungsi_satu(): # variabel x jadi bisa di akses oleh fungsi_dua
    global x
    x = 7
    
def fungsi_dua(n):
    return n+x

x = 3
print(x)
print(fungsi_dua(5))

fungsi_satu()
print(fungsi_dua(5))
