"""
Author: Manuel Brito
Program that make a division with two numbers and if the denominator is zero show a advise
"""

try:
    print("--Programa que realiza la división--\n")
    
    n1 = int(input("Dime un número entero: "))
    n2 = int(input("Dime otro número entero: "))

    if n2 == 0:
        print("El denominador no puede ser cero")
    else:
        print(f"La división de {n1} y {n2} es {round((n1/n2), 2)}")

except:
    print("Error")













