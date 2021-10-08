string = input()

string = string.lower()

a = True
for i in range(len(string)-1):
    for j in range(len(string)-1):
        if string[i] == string[i+1]:
            a = False
            break

if a == True :
    print('YA')
else:
    print('TIDAK')
