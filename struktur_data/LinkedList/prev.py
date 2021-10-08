# mw dibuat double linked list , tinggal ditambahin untuk next, push pop nya diganti dibedain sama yang prev diganti juga classnya bukan stack 
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        dataBaru = Node(data)
        if self.head == None:
            self.head = dataBaru
            self.tail = dataBaru
        else:
            dataBaru.prev = self.tail
            self.tail = dataBaru

    def pop(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            
    def display(self):
        temp = self.tail
        while temp != None:
            print(temp.data, end='')
            temp = temp.prev

    def peek(self):
        return self.tail

kata = input()
tumpukan = Stack()
for i in kata:
    tumpukan.push(i)
tumpukan.display()