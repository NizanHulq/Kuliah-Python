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

    def getCountLeaf(self):
        if self.root is None:
            return 0
        else:
            if self.root.left.root is None and self.root.right.root is None:
                return 1
            else:
                return self.root.left.getCountLeaf() + self.root.right.getCountLeaf()

tree = BST()

n = int(input())
array = list(map(int,input().split()))
for i in range(n):
    tree.insert(array[i])

print(tree.getCountLeaf())
