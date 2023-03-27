# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 19:59:12 2023

@author: acer
"""

try:
    x=int(input("Ingrese un numero: "))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("Lo siento, no puedes dividir para cero.")
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh querida, algo salio mal...")
print("FIN")