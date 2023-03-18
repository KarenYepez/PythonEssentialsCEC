# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:56:35 2023

@author: acer
"""

lista = ["R1","R2","R3",
         "S1","S2","S3"]
lista2=[]

'''print(len(lista))
print(lista[0])
print(lista[5])

for item in lista:
    #print(item)
    print(item,end=" * ")'''

'''
for item in lista:
    if "R" in item: #Detecta solo aquellos elementos que tengan la letra R
        print(item,end=" * ")
    elif "S" in item: #Detecta solo aquellos elementos que tengan la letra R
        print(item,end=" - ")
'''

for item in lista:
    if "R" in item: #Detecta solo aquellos elementos que tengan la letra R
        lista2.append(item) #Envia los datos con R de la lista y lo guarda en lista2 
        #print(item,end=" * ")