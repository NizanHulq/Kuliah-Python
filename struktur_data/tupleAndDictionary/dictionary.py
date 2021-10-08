nama_dictionary = {
    "kunci1": "nilai",
    "kunci2": "nilai",
    "kunci3": "nilai"
}

nama = {
    "nama1": "nizan",
    "nama2": "abdul",
    "nama3": "agus"
}
print(nama['nama2'])

nama = {
    "nama1": "nizan",
    "nama2": "abdul",
    "nama3": "agus"
}

print(nama.keys())
print(nama.values())

nama = {
    "nama1": "nizan",
    "nama2": "abdul",
    "nama3": "agus"
}
nama["nama4"] = "bagas"
print(nama)

nama = {
    "nama1": "nizan",
    "nama2": "abdul",
    "nama3": "agus"
}

del(nama["nama3"])
print(nama)

nama = {
    "nama1": "nizan",
    "nama2": "abdul",
    "nama3": "agus"
}

if 'nama4' in nama:
    print(True)
else:
    print(False)

nama = {
    "nama1": "nizan",
    "nama2": "abdul",
    "nama3": "agus"
}

nama["nama1"] = "gilang"
print(nama)
