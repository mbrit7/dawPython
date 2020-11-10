"""
Author: Manuel Brito
Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables
"""

try:
    a = int(input("Dime el valor entero de a: "))
    b = int(input("Dime el valor entero de b: "))

    a,b = b,a

    print(f"El valor anterior de a era {a} y ahora es {b} \nEl valor de b era {b} y ahora es {a}")

except:
    print("ERR0R")









