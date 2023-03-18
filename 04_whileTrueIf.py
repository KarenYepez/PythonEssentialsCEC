# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 19:34:00 2023

@author: acer
"""

num_cont=input("Ingrese el # al que debo contar: ")
num_cont=int(num_cont)
contador=1

print("Antes del While")
while(True):
    print(contador)
    contador+=1
    if contador>num_cont:
        break
    print("Dentro del bucle")
print("Fin del programa")

''' Mal identado el Break entra y sale del bucle en una sola pasada
print("Antes del While")
while(True):
    print(contador)
    contador+=1
    if contador>num_cont:
        pass
    break
    print("Dentro del bucle")
print("Fin del programa")
'''