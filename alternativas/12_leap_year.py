"""
Author: Manuel Brito
Program that show if a year is leap.
"""

# A year is leap when division with four is zero, but not if the division with one houndred is zero
# but if the division with one houndred and four houndred is zero, the year is leap.

try:
    print("--- Programa que te dice si un año es bisiesto---\n")

    year = int(input("Dime un año: "))
    
    if (year % 4 == 0):
        print(f"\n{year} es bisiesto")
    elif (year % 100 == 0 and year % 400 == 0):
        print(f"\nEl año {year} es bisiesto") 
    else:
        print(f"\n{year} no es bisiesto")
except:
    print("Err0r")









