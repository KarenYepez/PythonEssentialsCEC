# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:45:42 2023

@author: acer
"""

def crealista(n):
    lista=[]
    for item in range(1,n+1):
        lista.append(item)
    return lista

resultado=crealista(15)
print(resultado)