def createStack():
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

stack = createStack()
push(stack, "kambing")
push(stack, "kambing")
push(stack, "kambing")
push(stack, "kambing")
pop(stack)
display(stack)