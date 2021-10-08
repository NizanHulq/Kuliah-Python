class Node:
    def __init__ (self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push(self, data):
        dataBaru = Node(data) # membuat node baru
        # jika head belum ada datanya(None) atau Linkedlist masih kosong, maka head dan tailnya akan diisi oleh data baru 
        if self.head == None:
          self.head = dataBaru # head nya berubah menjadi node dataBaru
          self.tail = dataBaru # tail nya berubah menjadi node dataBaru

        # jika data sebelumnya sudah ada, maka 
        else:
          self.tail.next = dataBaru # tail.next data lama berubah menjadi dataBaru 
          self.tail = dataBaru
    
    def pop(self):
      # jika linked list dalam keadaan kosong
        if self.head == None:
            self.head = None
            self.tail = None
            return "tidak"

        # menandakan data hanya 1 bisa head=tail atau head.next = None
        elif self.head == self.tail:
            self.head = None
            self.tail = None 
        else:
            temp = self.head
            while(temp.next.next != None): # ketika urutan kedua setelah head/temp belum none maka head akan berubah menjadi head.next atau headnya akan maju terus satu node ke depan
                temp = temp.next # mengubah sementara head dari linked list sampai ke urutan kedua dari belakang atau sampai sebelum tail

            self.tail = temp # mengubah tail menjadi temp(node sebelum tail)
            self.tail.next = None
    
    def display(self):
        p = self.head
        lis = []
        while p is not None:
            lis.append(p.data)
            p = p.next
        return " ".join(list(map(str,lis)))

    def display3(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next

    def powpush(self,y,data):
        for i in range(y):
            dataBaru = Node(data) # membuat node baru
            # jika head belum ada datanya(None) atau Linkedlist masih kosong, maka head dan tailnya akan diisi oleh data baru 
            if self.head == None:
              self.head = dataBaru # head nya berubah menjadi node dataBaru
              self.tail = dataBaru # tail nya berubah menjadi node dataBaru

            # jika data sebelumnya sudah ada, maka 
            else:
              self.tail.next = dataBaru # tail.next data lama berubah menjadi dataBaru 
              self.tail = dataBaru
    def powpop(self,y):
        for i in range(y):    
            if self.head == None:
                 self.head = None
                 self.tail = None
                 return "tidak"

             # menandakan data hanya 1 bisa head=tail atau head.next = None
            elif self.head == self.tail:
                self.head = None
                self.tail = None 
            else:
                temp = self.head
                while(temp.next.next != None): # ketika urutan kedua setelah head/temp belum none maka head akan berubah menjadi head.next atau headnya akan maju terus satu node ke depan
                    temp = temp.next # mengubah sementara head dari linked list sampai ke urutan kedua dari belakang atau sampai sebelum tail
    
                self.tail = temp # mengubah tail menjadi temp(node sebelum tail)
                self.tail.next = None


stack = Stack()
stack2 = Stack()


baris1 = int(input())


for i in range(baris1):
    baris = input().split()
    if len(baris) == 1:
        perintah = baris[0]
        if perintah == "POP":
            POP = stack.pop()
            if POP == "tidak":
                stack2.push("ERROR: STACK KOSONG")
            else:
                hasil = "[ "+stack.display()+" ]"
                stack2.push(hasil)
    elif len(baris) == 2:
        perintah = baris[0]
        if perintah == "PUSH":
            x = int(baris[1])
            stack.push(x)
            hasil = "[ "+stack.display()+" ]"
            stack2.push(hasil)
        elif perintah == "POWPOP":
            y = int(baris[1])
            POP = stack.powpop(y)
            if POP == "tidak":
                stack2.push("ERROR: STACK KOSONG")
            else:
                hasil = "[ "+stack.display()+" ]"
                stack2.push(hasil)
    elif len(baris) == 3:
        perintah = baris[0]
        y = int(baris[1])
        x = int(baris[2])
        if perintah == "POWPUSH":
            stack.powpush(y,x)
            hasil = "[ "+stack.display()+" ]"
            stack2.push(hasil)

stack2.display3()




        
        

    

    
    
    
    








