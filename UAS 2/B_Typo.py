# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 13:01:11 2021

@author: LENOVO
"""

passw = input()
ketikPass = input()

lisPassw = [None]*100
for i in range(len(passw)):
    lisPassw[i] = passw[i]
    
lisKetikPass = [None]*100
for i in range(len(ketikPass)):
    lisKetikPass[i] = ketikPass[i]

typo = 0
for cek in range(100):
    if lisPassw[cek] != lisKetikPass[cek]:
        typo += 1


if typo > 1:
    print("tidak")
else:
    print("ya")

