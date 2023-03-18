# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:43:40 2023

@author: acer
"""

nombre = input("Ingrese su nombre: ") #Hago conversion de datos
apellido = input("Ingrese su apellido: ")
#direccion = input("Ingrese su direccion: ")
edad = int(input("Ingrese su edad: "))

print("\n"*2)
space=" "
NC=nombre+space+apellido

print(NC)
if edad>=0:
    if edad<=5:
        print("Se encuentra en la primera infancia.")
    elif edad>=6 and edad<=11:
        print("Se encuentra en la etapa de la infancia")
    elif edad>=12 and edad<=18:
        print("Se encuentra en la etapa de la adolescencia")
    elif edad>=18 and edad<=26:
        print("Se encuentra en la etapa de la juventud")
    elif edad>=27 and edad<=59:
        print("Se encuentra en la etapa de la adultez")
    elif edad>=60:
        print("Se encuentra en la etapa de la vejez")
else:
    print("Ha ingresado una edad no valida")
