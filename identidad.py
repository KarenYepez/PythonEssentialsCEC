# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:37:06 2019

@author: UPS
"""
import numpy as np
identidad1 = np.eye(4,6) #Entrega 1s en la diagonal, lo demas cero, pero de cualquier dimension 
print(identidad1)
print("\n"*2)
identidad2 = np.identity(5) #Matriz identidad - Siempre cuadrada
print(identidad2)