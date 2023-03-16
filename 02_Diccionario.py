# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 20:17:29 2023

@author: acer
"""

dict1={1001:"Juan Carlos",
       "email":"jdominguez@cec-epn.edu.ec",
       "emp1":"Juan",
       #"emp1":"Carlos" ERROR POR DEFINIR DOS VECES
       "R1":"10.10.10.1",
       "AP":"10.10.11.1",
       "emp1":"Carlos", #Se almacena lo ultimo guardado en la llave
       "ECivil":True,
       "saldo":[1, 2, 3, 4, 5]
       }

print(dict1["emp1"])
print(dict1)
print("S1" in dict1) #Indica si hay esa cadena dentro del diccionario
print("saldo" in dict1) #Indica si hay esa cadena dentro del diccionario