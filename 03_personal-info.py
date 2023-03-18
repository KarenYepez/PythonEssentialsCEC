# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 18:31:07 2023

@author: acer
"""
print("\n")
print("BOLETO PARA LA GRAN RIFA")
nombre = input("Ingrese su nombre: ") #Hago conversion de datos
apellido = input("Ingrese su apellido: ")
direccion = input("Ingrese su direccion: ")
edad = int(input("Ingrese su edad: "))
celular = input("Ingrese su numero celular: ")
print("\n"*2)
space=" "
NC=nombre+space+apellido
print("El boleto ganador con el número 514 pertenece a: ", NC,"que tiene", edad, "años, y vive en el sector de ", direccion)
print("Se procede a realizar la llamada a su celular: ",celular)
