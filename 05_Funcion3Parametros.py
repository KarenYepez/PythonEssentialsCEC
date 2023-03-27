# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 18:48:18 2023

@author: acer
"""

def address(calle,ciudad,codPostal):
    print("La pizza debe ser entregada en la calle",calle,"de la ciudad de",ciudad,". Código postal",codPostal)

cl=input("Ingrese la calle: ")
cp=input("Ingrese el código postal: ")
ct=input("Ingrese la ciudad: ")

address(cl, ct, cp)