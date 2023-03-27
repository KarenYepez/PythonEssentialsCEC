# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 20:58:39 2023

@author: acer
"""

def isYearLeap(year):
    year=int(year)
    bisies = year%4
    secul = year%400
    cent = year%100
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
    
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]

for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")