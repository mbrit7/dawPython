"""
Author: Manuel Brito
Program that input two numbers and show if the first is or isn't greater than the second.
"""

try:
    print("-- Programa que muestra si un número es mayor que otro --") 

    num1 = int(input("\nDime un número: "))
    num2 = int(input("Dime otro número: "))
    
    if num1 > num2:
        print(f"\n{num1} es mayor que {num2}")
    else:
        print(f"{num2} es mayor que {num1}")

except:
    print("ERRoR")












