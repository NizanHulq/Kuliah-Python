class Node: # membuat class node terlebih dahulu
    def __init__(self, angka=None): # membuat konstruktor dengan atribut data, left dan right
        self.angka = angka
        self.left =None
        self.right = None

class BST: # membuat class tree 
    def __init__(self): # konstruktor dengan atribut root
        self.root = None

    def insert(self, angka):
        if self.root == None:
            nodeBaru = Node(angka)
            self.root = nodeBaru
            self.root.left = BST()
            self.root.right = BST()
        else:
            if self.root.angka > angka:
                self.root.left.insert(angka)
            else:
                self.root.right.insert(angka)
                
                
    def preOrder(self):
        if self.root is not None:
            print(self.root.angka)
            self.root.left.preOrder()
            self.root.right.preOrder()
            
    def inOrder(self):
        if self.root is not None:
            self.root.left.inOrder()
            print(self.root.angka)
            self.root.right.inOrder()

    def postOrder(self):
        if self.root is not None: 
            self.root.left.postOrder()
            self.root.right.postOrder()
            print(self.root.angka)

    def getTinggi(self):
        if self.root is None:
            return -1
        else:
            return 1 + max(self.root.left.getTinggi() , self.root.right.getTinggi())
        
    def getCountNode(self):
        if self.root is None:
            return 0
        else:
            return 1 + self.root.left.getCountNode() + self.root.right.getCountNode()
    
    def getSumNode(self):
        
        if self.root is None:
            return 0
        else:
            return  self.root.angka + self.root.left.getSumNode() + self.root.right.getSumNode()

    def getAverageNode(self): 
        return self.getSumNode() / self.getCountNode()

    def getCountLeaf(self):
        if self.root is None:
            return 0
        else:
            if self.root.left.getTinggi() and self.root.left.getTinggi() == -1:
            # if self.root.left.root is None and self.root.right.root is None:
                return 1
            else:
                return self.root.left.getCountLeaf() + self.root.right.getCountLeaf()

    def getSumLeaf(self):
        if self.root is None:
            return 0
        elif self.root.left.getTinggi() and self.root.left.getTinggi() == -1:
            return self.root.angka
        else:
            return self.root.left.getSumLeaf() + self.root.right.getSumLeaf()

    def getMaxNode(self):
        if self.root is not None:
            if self.root.right.root is not None:
                return self.root.right.getMaxNode()
            else:
                return self.root.angka

    def getMinNode(self):
        if self.root is not None:
            if self.root.left.root is not None:
                return self.root.left.getMinNode()
            else:
                return self.root.angka 

    def getCountNodeDengan1Anak(self):
        if self.root is None:
            return 0
        elif self.root.left.root is not None and self.root.right.root is None:
            return 1 + self.root.left.getCountNodeDengan1Anak() + self.root.right.getCountNodeDengan1Anak()
        elif self.root.left.root is None and self.root.right.root is not None:
            return 1 + self.root.left.getCountNodeDengan1Anak() + self.root.right.getCountNodeDengan1Anak()  
        else:
            return self.root.left.getCountNodeDengan1Anak() + self.root.right.getCountNodeDengan1Anak()

    def getCountNodeDengan2Anak(self):
        if self.root is None:
            return 0
        elif self.root.left.root is not None and self.root.right.root is not None:
            return 1 + self.root.left.getCountNodeDengan2Anak() + self.root.right.getCountNodeDengan2Anak()
        else:
            return self.root.left.getCountNodeDengan2Anak() + self.root.right.getCountNodeDengan2Anak()
        
    def getCountNodeGenap(self):
        if self.root is None:
            return 0
        else:
            if self.root.angka%2 == 0:
                return 1 + self.root.left.getCountNodeGenap() + self.root.right.getCountNodeGenap()
            else:
                return self.root.left.getCountNodeGenap() + self.root.right.getCountNodeGenap()

    def getCountNodeGanjil(self):
        if self.root is None:
            return 0
        else:
            if self.root.angka%2 != 0:
                return 1 + self.root.left.getCountNodeGanjil() + self.root.right.getCountNodeGanjil()
            else:
                return self.root.left.getCountNodeGanjil() + self.root.right.getCountNodeGanjil()

    def getSumNodeGenap(self):
        if self.root is None:
            return 0
        else:
            if self.root.angka%2 == 0:
                return self.root.angka + self.root.left.getSumNodeGenap() + self.root.right.getSumNodeGenap()
            else:
                return self.root.left.getSumNodeGenap() + self.root.right.getSumNodeGenap() 

    def getSumNodeGanjil(self):
        if self.root is None:
            return 0
        else:
            if self.root.angka%2 != 0:
                return self.root.angka + self.root.left.getSumNodeGanjil() + self.root.right.getSumNodeGanjil()
            else:
                return self.root.left.getSumNodeGanjil() + self.root.right.getSumNodeGanjil()
    
pohon = BST()
pohon.insert(4)   
pohon.insert(2)     
pohon.insert(5)
pohon.insert(3)


pohon.preOrder()
print("===getTinggi")
print(pohon.getTinggi())
print("===getCountNode")
print(pohon.getCountNode())
print("===getSumNode")
print(pohon.getSumNode())
print("===getCountLeaf")
print(pohon.getCountLeaf())
print("===getSumLeaf")
print(pohon.getSumLeaf())
print("===getAverageNode")
print(pohon.getAverageNode())
print("===getMaxNode")
print(pohon.getMaxNode())
print("===getMinNode")
print(pohon.getMinNode())
print("===getCountNodeDengan1Anak")
print(pohon.getCountNodeDengan1Anak())
print("===getCountNodeDengan2Anak")
print(pohon.getCountNodeDengan2Anak())
print("===getCountNodeGenap")
print(pohon.getCountNodeGenap())
print("===getCountNodeGanjil")
print(pohon.getCountNodeGanjil())
print("===getSumNodeGenap")
print(pohon.getSumNodeGenap())
print("===getSumNodeGanjil")
print(pohon.getSumNodeGanjil())