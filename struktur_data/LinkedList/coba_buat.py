# membuat node

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

# membuat linked list queue
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self,data):
        dataBaru = Node(data)
        if self.head == None:
            self.head = dataBaru
            self.tail = dataBaru
        else:
            self.tail.next = dataBaru
            self.tail = dataBaru
    
    def remove(self):

        if self.head == self.tail:
            self.tail = None
            self.head = None
        elif self.head == None:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.next
    
    def display(self): #menjelajahi dari satu node ke node yang lain
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next

linkedCoba = LinkedList()

linkedCoba.add('ayam')
linkedCoba.add('abe')
linkedCoba.add('itu')
linkedCoba.add('dari')

linkedCoba.display()

linkedCoba.remove()
linkedCoba.remove()
linkedCoba.remove()
linkedCoba.remove()
linkedCoba.remove()

print('====')
linkedCoba.display()