# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:01:41 2023

@author: acer
"""

def isYearLeap(year):
    year=int(year)
    bisies = year%4
    secul = year%400
    cent = year%100
    
    if cent ==0 and secul != 0:
        resultado = False
    elif bisies == 0:
        resultado = True
    else:
        resultado = False
    return resultado

def daysInMonth(year, month):
    abis = isYearLeap(year)
    meses = [1,2,3,4,5,6,7,8,9,10,11,12]
    meses31 = [1,3,5,7,8,10,12]
    meses30 = [4,6,9,11]
    
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
    

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
