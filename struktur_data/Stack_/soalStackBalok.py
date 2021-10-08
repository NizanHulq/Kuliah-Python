class Node:
    def __init__ (self, nama=None, nomor=None):
        self.nama = nama
        self.nomor = nomor
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push(self, balok):
        dataBaru = Node(balok.nama, balok.nomor)
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
            print(p.nama)
            p = p.next

    def peek(self):
        return self.head
    
    
pakuA = Stack()
pakuB = Stack()
pakuC = Stack()


b1 = Node("balok1", 1)
b2 = Node("balok2", 2)
b3 = Node("balok3", 3)
b4 = Node("balok4", 4)

pakuB.push(b4)
pakuB.push(b3)
pakuB.push(b2)
pakuB.push(b1)

def pindah(pakuAsal, pakuTujuan):
    temp = pakuAsal.peek()
    pakuAsal.pop()
    pakuTujuan.push(temp)

def displayAll():
    print("==Paku A==")
    pakuA.display()
    print("----------")
    print("==Paku B==")
    pakuB.display()
    print("----------")
    print("==Paku C==")
    pakuC.display()
    print("----------")

displayAll()
    
pindah(pakuB,pakuC)
pindah(pakuB,pakuA)
pindah(pakuC,pakuA)
pindah(pakuB,pakuC)
pindah(pakuA,pakuB)
pindah(pakuA,pakuC)
pindah(pakuB,pakuC)
pindah(pakuB,pakuA)
pindah(pakuC,pakuA)
pindah(pakuC,pakuB)
pindah(pakuA,pakuB)
pindah(pakuC,pakuA)
pindah(pakuB,pakuC)
pindah(pakuB,pakuA)
pindah(pakuC,pakuA)

print("===setelah dipindah===")
displayAll()




