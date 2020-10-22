"""
Author: Manuel Brito
Program that show if a number is even or not.
"""

try:
    print("-- Programa que muestra si el número es par o impar --\n")    

    n1 = int(input("Dime un número entero: "))
    
    if n1 % 2 == 0:
        print(f"\n{n1} es un número par") 
    else:
        print(f"{n1} no es par")

except:
    print("Error")










