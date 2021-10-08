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

def operasi(operator,angka1,angka2):
    if operator =='*':
        return int(angka1) * int(angka2)
    elif operator =='/':
        return int(angka1)/int(angka2)
    elif operator == '+':
        return int(angka1) + int(angka2)
    elif operator == '-':
        return int(angka1) - int(angka2)

postfix = input('masukkan operasi postfix : ').split()
operan = Stack(50)
for i in postfix: # 1
    if i in ['0','1','2','3','4','5','6','7','8','9']: # 2
        operan.push(int(i))
    else: # 3
        angka2 = operan.pop() 
        angka1 = operan.pop()
        hasil = operasi(i,angka1,angka2)
        operan.push(hasil)
print('hasil operasi postfix : ',operan.pop()) 



