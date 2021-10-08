# ini membuat class stack
class Stack:
    def __init__(self,max):
        self.top = -1
        self.stackSize = max
        self.datum = []
    def isEmpty(self):
        if self.top == -1:
            return True
        else: 
            return False
    def isFull(self):
        if self.top == self.stackSize-1 :
            return True
        else:
            return False
    def push(self, datum):
        if self.top == self.stackSize-1 :
            self.top = self.top    
        else:
            self.top = self.top + 1 
            self.datum.insert(self.top,datum)
    def pop(self):
        if self.top == -1:
            self.top = self.top
        else:  
          self.top = self.top - 1
          return self.datum.pop(self.top+1)
    def peek(self):
        if self.top == -1:
            self.top = self.top
        else:
          return self.datum[self.top]  

# ini mulai masuk ke algoritma cara mengkonversi dari infix ke postfix
# operator yang digunakan hanya +,-,*,/ 
def prioritas(komponen):
    if komponen == '*' or komponen == '/' :
        return  3
    elif komponen == '+' or komponen == '-' :
        return  2
    elif komponen == '(' or komponen ==  ')' :
        return  1
    else:
        return 1

# input harus pake spasi
infix = input('masukkan operasi infix(batasan operator "+ , - , * , /" ) : ').split()
postfix = []
operator = Stack(50)

# untuk memasukkan setiap anggota list infix ke dalam list opstfix atau stack operator
for i in infix :
    if i in "1234567890" : # 1
        postfix.append(i)
    else:
        if operator.isEmpty() == True: # 2
            operator.push(i)
        else:
            if i == '(' :    # 3
                operator.push(i)
            elif i == ')' :      # 4
                while operator.peek() != '(':
                    postfix.append(operator.pop())
                operator.pop()
            elif i in ['+','-','*','/'] :     # 5
                 if  operator.isEmpty() != True:
                    if prioritas(i) <= prioritas(operator.peek()): # 6
                         postfix.append(operator.pop())
                         operator.push(i)
                    else:
                       operator.push(i)
            else:   # 7
                 operator.push(i)

while operator.isEmpty() != True:
    postfix.append(operator.pop())
print('operasi postfix : ',' '.join(postfix))
    

     




