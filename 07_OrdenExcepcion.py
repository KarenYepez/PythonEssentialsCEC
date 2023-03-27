# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 20:10:17 2023

@author: acer
"""

try:
    y=1/0
   
except ZeroDivisionError:
    print("Lo siento, no puedes dividir para cero.")
except ArithmeticError:
    print("Problema Aritmético")

print("FIN")
    

'''
except ArithmeticError:
    print("Problema Aritmético")
except ZeroDivisionError:
    print("Lo siento, no puedes dividir para cero.")'''