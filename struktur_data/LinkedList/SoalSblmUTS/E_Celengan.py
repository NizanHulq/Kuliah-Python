
class Node:
  
  def __init__(self, data = None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  
  def addBelakang(self, data):
    dataBaru = Node(data) 
   
    if self.head == None:
      self.head = dataBaru 
      self.tail = dataBaru 
    
    
    else:
      self.tail.next = dataBaru 
      self.tail = dataBaru 



    
  def addDepan(self,data):
    dataBaru = Node(data) 
    if self.head == None: 
        self.head = dataBaru 
        self.head.next = dataBaru 
        self.tail = dataBaru 
        
    else:
          temp = self.head 
          self.head = dataBaru 
          self.head.next = temp 

  def removeHead(self):
   
    if self.head == None:
     self.head = None
     self.tail = None 
    elif self.head == self.tail:
      self.head = self.head.next
      self.tail = None
    else:
        self.head = self.head.next


  def removeTail(self):
    if self.head == None:
     self.head = None
     self.tail = None

    elif self.head == self.tail:
        self.head = None
        self.tail = None 
    else:
        temp = self.head
        while(temp.next.next != None): 
            temp = temp.next 
        
        self.tail = temp 
        self.tail.next = None 

  def display(self):
    p = self.head
    lis = []
    while p is not None:
        lis.append(p.data)
        p = p.next
    return lis

celengan = LinkedList()



baris1 = int(input())

for i in range(baris1):
    kegiatan = input().split()
    parameter = kegiatan[0]
    x = int(kegiatan[1])
    if parameter == "0":
        celengan.addDepan(x)
    elif parameter == "1":
        celengan.addBelakang(x)
    elif parameter == "2":
        celengan.removeTail()  
    elif parameter == "3":
        celengan.removeHead()

isiCelengan = celengan.display()


total = 0
for j in isiCelengan:
    total = total + j
print(total)








