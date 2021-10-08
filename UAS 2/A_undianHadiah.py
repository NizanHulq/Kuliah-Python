# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 12:42:20 2021

@author: LENOVO
"""

inp = input().split()

n = int(inp[0])
x = int(inp[1])

kuponPel = []
for kupon in range(n):
    kuponPel.append(int(input()))
    
selisih =[]
for itungSelisih in kuponPel:
    if itungSelisih > x:
        selisih.append(itungSelisih - x)
    else:
        selisih.append((x - itungSelisih))
        
print(selisih.count(min(selisih)))

