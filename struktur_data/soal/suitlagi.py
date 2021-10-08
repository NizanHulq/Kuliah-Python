blangkon = input()
semar = input()

if blangkon == semar:
        print('Seri')
elif blangkon == '[]' :
    if semar == '()':
        print('Blangkon')
    else:
        print('Semar')
elif blangkon == '()' :
    if semar == '8<':
        print('Blangkon')
    else:
        print('Semar')
elif blangkon == '8<' :
    if semar == '[]':
        print('Blangkon')
    else:
        print('Semar') 

        