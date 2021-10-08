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
        lis = []
        while p is not None:
            lis.append(p.data)
            p = p.next
        return lis

    def peek(self):
        return self.head


biner = Stack()

angkaBiner = input()

for i in angkaBiner:
    biner.push(i)

bulat = 0
pangkat = 0
angka = list(map(int,biner.display()))

for j in angka:
    bulat += j*2**pangkat
    pangkat += 1

print(bulat)



