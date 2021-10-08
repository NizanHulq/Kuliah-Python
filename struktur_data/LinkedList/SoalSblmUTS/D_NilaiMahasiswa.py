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
            
    def display(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next


    

stack = Stack()
baris1 = int(input())
baris2 = list(map(int,input().split()))

for nilai in baris2:
    if nilai >= 0 and nilai <= 100:
        stack.push(nilai)
stack.display()


