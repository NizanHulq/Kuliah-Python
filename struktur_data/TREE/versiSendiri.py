# binary search tree
class Node:
    def __init__(self, data=None):
        self.data = data
        

class Tree: # lebih baik konsep nya left sama right melekat di class Node sehingga untuk yang lebih kompleks tidak menjadi masalah
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None
        
    def insert(self,angka):
        if self.root is None:
            nodeBaru = Node(angka)
            self.root = nodeBaru
            self.left = Tree()
            self.right = Tree()      

        else:
            if self.root.data > angka:
                self.left.insert(angka)
            else:
                self.right.insert(angka)  
                
    
    def preOrder(self):
        if self.root is not None:
            print(self.root.data)
            self.left.preOrder()
            self.right.preOrder()


pohon = Tree()

pohon.insert(5)
pohon.insert(6)
pohon.insert(4)
pohon.insert(3)
pohon.insert(2)

pohon.preOrder()




        
