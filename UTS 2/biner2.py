import sys

def Stack():
    lis=[]
    return lis

def push(S, data):
    S.append(data)

def pop(S):
    S.pop()

def isEmpety(S):
    if len(S) == 0:
        return True
    else:
        return False

def display(S):  
    print(S)


def peek(S):
    return S[-1]


def clear(S):
    S.clear()

biner = Stack()

angkaBiner = input()

for i in angkaBiner:
    push(biner,i)

angka = list(map(int,biner))

bulat = 0
pangkat = len(biner)-1

for j in angka:
    bulat += j*2**pangkat
    pangkat -= 1
    
sys.stdout.write(str(bulat))