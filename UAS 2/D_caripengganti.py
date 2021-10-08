# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 13:36:30 2021

@author: LENOVO
"""

panjangList = int(input())
tree = list(map(int,input().split()))
hapus = int(input())

treeUrut = sorted(tree)

if hapus == treeUrut[0]:
    print(-1)
else:
    print(treeUrut[treeUrut.index(hapus) - 1])
    
    