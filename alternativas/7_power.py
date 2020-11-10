"""
Author: Manuel Brito
Program that realize the power of one number with the exponent and the base.
1. if the exponent is positive, print the power
2. if the exponent is zero, the result is one
3. if the exponent is negative, the result is 1/power with the positive exponent.
"""

from math import pow

try:
    print("Programa que calcula la potencia de un número\n")

    base = int(input("Dime la base de la potencia: "))
    exponent = int(input("Dime el exponente de la potencia: "))

    # La potencia de un número se consigue multiplicando el número de la base 
    # tantas veces como el número del exponente
    if exponent > 0:
        print(f"\nEl resultado de la potencia con base {base} y exponente {exponent}  es igual a {pow(base, exponent)}")
    elif exponent == 0:
        print("\nEl resultado de la potencia es 1") 

    else:
        print(f"\nEl resultado de la potencia es 1/{pow(base, -exponent)}")


except:
    print("err0r")









