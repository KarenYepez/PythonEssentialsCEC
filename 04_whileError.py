# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 19:47:40 2023

@author: acer
"""

while True:
    x=input("Enter a number to count to: ")
    if x=="q" or x=="quit":
        break
    x=int(x) #Requeria identacion
    y=1
          
    while True:
        print(y)
        y=y+1
        if y>x:
            break
 