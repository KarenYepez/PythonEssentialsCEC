# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:56:57 2023

@author: acer
"""

#USO DE LISTAS
lista=["1",2,3.5,True,"1"]
print(type(lista))
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista[-5]) #Equivale a la posicion 0
print(lista[-2]) #Equivale a la posicion 3
lista[4]="4"
del lista[4] #BORRA EL ELEMENTO


#USO DE LA TUPLA  
tupla=("1",2,3.5,True,"1")
print(type(tupla))
print(tupla[0])
print(tupla[1])
print(tupla[2])
print(tupla[3])
print(tupla[4])
#tupla(4)="4"  OPERACION NO SOPORTADA POR INMUTABILIDAD
#del tupla(4) NO SOPORTADA
