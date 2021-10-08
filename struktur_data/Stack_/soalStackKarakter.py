class Node:
    def __init__ (self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push(self, data):
        dataBaru = Node(data)
        if self.head == None:
            self.head = dataBaru
            self.tail =  dataBaru
    
        else:
            temp = self.head 
            self.head = dataBaru 
            self.head.next = temp
        
    def pop(self):
        if self.head == None:
            self.head = None
            self.tail = None 
        elif self.head == self.tail:
          self.head = self.head.next
          self.tail = None
        else:
            self.head = self.head.next
            
    def display(self):
        p = self.head

        while p is not None:
            print(p.data, end=" ")
            p = p.next

    def peek(self):
        return self.head
        
    def isEmpety(self):
        if self.head == None:
            return True
        else:
            return False


karakter = Stack()

kalimat = input()


for i in kalimat:
    karakter.push(i)

karakter.display()


        

