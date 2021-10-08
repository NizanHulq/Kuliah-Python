nim = input()
pertanyaan = input()
nim = nim.split('/')

if pertanyaan == 'angkatan':
    print(nim[0])
elif pertanyaan == 'NIU':
    print(nim[1])
elif pertanyaan == 'fakultas':
    print(nim[2])
elif pertanyaan == 'NIF':
    print(nim[3])