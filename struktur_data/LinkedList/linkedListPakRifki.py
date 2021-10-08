# Kelas Node
class Node:
  # __ adalah private class
  def __init__(self, data = None):
    self.data = data
    self.next = None

# Kelas LinkedList
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  # Menambahkan data baru dari belakang
  def addBelakang(self, data):
    dataBaru = Node(data) # membuat node baru
    # jika head belum ada datanya(None) atau Linkedlist masih kosong, maka head dan tailnya akan diisi oleh data baru 
    if self.head == None:
      self.head = dataBaru # head nya berubah menjadi node dataBaru
      self.tail = dataBaru # tail nya berubah menjadi node dataBaru
    
    # jika data sebelumnya sudah ada, maka 
    else:
      self.tail.next = dataBaru # tail.next data lama berubah menjadi dataBaru 
      self.tail = dataBaru # tail linked list berubah dari data lama menjadi dataBaru 



    # menambahkan data baru dari depan
  def addDepan(self,data):
    dataBaru = Node(data) # membuat node baru
    # jika linked list masih kosong atau head=None
    if self.head == None: 
        self.head = dataBaru # head linked list akan berubah menjadi dataBaru
        self.head.next = dataBaru # head.next akan menjadi dataBaru
        self.tail = dataBaru # tail linked list akan berubah menjadi dataBaru
        
    else:
          temp = self.head # menyimpan head lama dalam variabel 
          self.head = dataBaru # mengubah head lama ke dataBaru
          self.head.next = temp # mengubah head.next data baru ke temp(head lama)



  # Menghapus data dari headnya 
  def removeHead(self):
   
    if self.head == None:
     self.head = None
     self.tail = None 
    elif self.head == self.tail:
      self.head = self.head.next
      self.tail = None
    else:
        self.head = self.head.next

    # menghapus data dari tail nya
  def removeTail(self):
      # jika linked list dalam keadaan kosong
    if self.head == None:
     self.head = None
     self.tail = None

    # menandakan data hanya 1 bisa head=tail atau head.next = None
    elif self.head == self.tail:
        self.head = None
        self.tail = None 
    else:
        temp = self.head
        while(temp.next.next != None): # ketika urutan kedua setelah head/temp belum none maka head akan berubah menjadi head.next atau headnya akan maju terus satu node ke depan
            temp = temp.next # mengubah sementara head dari linked list sampai ke urutan kedua dari belakang atau sampai sebelum tail
        
        self.tail = temp # mengubah tail menjadi temp(node sebelum tail)
        self.tail.next = None #  tail.next akan berubah menjadi none


  def remove2(self):
    if self.head is not None:
      if self.head == self.tail:
        self.head = None
        self.tail = None
      else:
        self.head == self.head.next

  # Menampilkan data kelas LinkedList
  def display(self):
    p = self.head
    # Jika p tidak None maka datanya akan ditampilkan(print)
    while p is not None:
      print(p.data,end=" => ")
      p = p.next

linkedCoba = LinkedList()

linkedCoba.addDepan('ikan')
linkedCoba.addBelakang('ayam')
linkedCoba.addDepan('mati')
linkedCoba.addDepan('hidup')
linkedCoba.addDepan('betina')
linkedCoba.addBelakang('ayam')

linkedCoba.removeTail()
linkedCoba.removeTail()
linkedCoba.removeTail()
linkedCoba.removeTail()










linkedCoba.display()

