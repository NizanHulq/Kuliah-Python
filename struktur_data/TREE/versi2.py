class Node:
    def __init__(self,data):
        self.data = data
        self.left =None
        self.right = None
    
    def insert(self,angka):
        if self.data is None:
            self.data = angka
        else:
            if self.data > angka: # cek kiri atau kanan
                if self.left is None:# cek kiri ada atau kosong
                    self.left = Node(angka) # bikin objek baru node
                else:
                    self.left.insert(angka)
            else:
                if self.right is None:# cek kiri ada atau kosong
                    self.right = Node(angka) # bikin objek baru node
                else:
                    self.right.insert(angka)

    def preOrder(self):
        print(self.data)
        if self.left is not None:
            self.left.preOrder()
        if self.right is not None:    
            self.right.preOrder()

    def inOrder(self):
        
        if self.left is not None:
            self.left.inOrder()
        print(self.data)
        if self.right is not None:    
            self.right.inOrder()
    
    def postOrder(self):
        if self.left is not None:
            self.left.postOrder()
        if self.right is not None:    
            self.right.postOrder()
        print(self.data)



root = Node(12)
root.insert(9)
root.insert(10)
root.insert(13)
root.insert(11)
root.preOrder()
