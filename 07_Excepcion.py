# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 19:48:47 2023

@author: acer
"""

print("Inicio")
try:
    print("uno")
    x = 1/0  #Esto error hace que salga del try pero no corta la ejecucion
    print("dos")
except:
    print("Algo no salió bien, hay un error")
    print("tres")
print("Fin de codigo")