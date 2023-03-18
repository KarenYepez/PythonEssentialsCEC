# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 23:28:58 2023

@author: acer
"""
#SOLUCIONADO POR: Karen Yépez

# Create a list of the BRICS countries
country = [ 
            "Brazil", 
            "Russia", 
            "India", 
            "China", 
            "South Africa"
          ]

"""Create a dictionary of BRICS capitals.
Note that South Africa has 3
 capitals. Therefore, we embed a list inside
the dictionary.
"""

capitals = {
    "Brazil": "Brasilia",
    "Russia": "Moscow",
    "India": "New Delhi",
    "China": "Beijing",
    "South Africa": [
                        "Pretoria",
                        "Cape Town",
                        "Bloemfontein"
                    ]
           }

# Print the list and dictionary
print(list(country)) #No reconocia a country como lista si no como string
print("\n"*2)
print(dict(capitals)) #No reconocia a country como diccionario si no como string
print("\n"*2)
"""
What response did you get?
   #country
   #capitals
Why did the list and dictionary
 contents not print? 
   #No definía a country como lista si no como string
   #No definía a capitals como diccionario si no como string
Fix the code and run the script again. 
   #Corregido
"""

print(capitals["South Africa"][1])
#print(capitals["South Africa"[1]]) ERROR
"""
Why did you get an error for the
 2nd capital of South Africa?
Hint: Check the syntax for the 
index value.
"""
