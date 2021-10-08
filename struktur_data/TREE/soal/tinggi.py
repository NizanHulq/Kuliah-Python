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

    def getTinggi(self):
        if self.root is None:
            return 0
        else:
            return 1 + max(self.root.left.getTinggi() , self.root.right.getTinggi())


tree = BST()

n = int(input())
array = list(map(int,input().split()))

for i in range(n):
    tree.insert(array[i])

print(tree.getTinggi())