# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 00:14:01 2023

@author: acer
"""

def isYearLeap(year):
    bisies = year%4
    secul = year%400
    cent = year%100
    
    #Validación de año
    if year >=0:
        if cent ==0 and secul != 0:
            resultado = False
        elif bisies == 0:
            resultado = True
        else:
            resultado = False
        return resultado
    else:
        return None

def daysInMonth(year, month):
    abis = isYearLeap(year)
    meses = [1,2,3,4,5,6,7,8,9,10,11,12]
    meses31 = [1,3,5,7,8,10,12]
    meses30 = [4,6,9,11]
    
    #Validación de mes
    if month in meses:
        if month in meses31:
            return 31
        elif month in meses30:
            return 30
        elif month == 2 and abis == True:
            return 29
        elif month == 2 and abis == False:
            return 28
        else:
            return None
    else:
        return None

def dayOfYear(year, month, day):
    #Validación de día
    valDay = daysInMonth(year, month)
    try:      
        if day>0 and day<=valDay:
            sumD = 0
            for m in range (1,month):
                sumD = sumD + daysInMonth(year, m)
            sumD = sumD + day
            return sumD
        else:
            return None
    except:
        return None

    
#Pruebas de Funcionamiento 
print(dayOfYear(2000, 12, 31)) #Ultimo dia en un año bisiesto
print(dayOfYear(2001, 12, 31)) #Ultimo dia en un año NO bisiesto
print(dayOfYear(2024, 1, 24)) #Dia 24 de enero (Total de dias: 24)
print(dayOfYear(3020, 2, 30)) #Dia 30 de febrero No existente
print(dayOfYear(2000, 2, 29)) #Dia 29 de febrero en un año bisiesto
print(dayOfYear(2011, 7, -2)) #Dia negativo No existente
print(dayOfYear(1920, 14, 1)) #Mes No existente
print(dayOfYear(-4582, 14, 1)) #Año No existente
print(dayOfYear(2023, 1, 1)) #Ultimo dia en un año bisiesto
