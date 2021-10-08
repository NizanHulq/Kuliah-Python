def createQueue():
    lis=[]
    return lis

def queue(S, data):
    #sama adengan add tail
    S.append(data)

def deque(S):
    if len(S) == 0:
        None
    else:
        S.pop(0)

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