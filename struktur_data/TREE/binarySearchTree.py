class Node: # membuat class node terlebih dahulu
    def __init__(self, data=None): # membuat konstruktor dengan atribut data, left dan right
        self.data = data
        self.left =None
        self.right = None

class Tree: # membuat class tree 
    def __init__(self): # konstruktor dengan atribut root
        self.root = None

    def insert(self,angka): # membuat method insert dengan parameter angka 
        if self.root is None: # jika self.root dalam keadaan kosong
            nodeBaru = Node(angka) # maka buat node baru
            self.root = nodeBaru # node baru akan menjadi root
            self.root.left = Tree() # lalu left dari node baru diubah menjadi sebuah tree dan yang right juga
            self.root.right = Tree()

        else: # jika root dalam keadaan isi
            if self.root.data > angka: # maka jika data dalam root > dari angka 
              self.root.left.insert(angka) # maka tree left akan insert angka sehingga akan mengulang kembali ke syarat pertama method insert
            else: # jika data dalam root lebih kecil atau sama dengan dari angka
                self.root.right.insert(angka)  # maka akan melakukan rekursi insert kepada tree right
    
    def preOrder(self): # preorder urutannya adalah jika root tidak kosong maka akan print data lalu print left dengan rekursi, dan print right dengan rekursi
        if self.root is not None:
            print(self.root.data)
            self.root.left.preOrder()
            self.root.right.preOrder()
    
    def inOrder(self): # inorder hanya berbeda urutan dengan preorder yaitu  print left dulu, lalu print data, lalu right 
        if self.root is not None:
            self.root.left.inOrder()
            print(self.root.data)
            self.root.right.inOrder()
    
    def postOrder(self):
        if self.root is not None: # print left dulu lalu right, kemudian data
            self.root.left.postOrder()
            self.root.right.postOrder()
            print(self.root.data)


pohon = Tree()

pohon.insert(5)
pohon.insert(6)
pohon.insert(4)
pohon.preOrder()
print("=====")
pohon.inOrder()
print("====")
pohon.postOrder()




        
