"""
Author: Manuel Brito
Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
"""

try:
    name = input("Dime tu nombre: ")
    surname = input("Dime tu primer apellido: ")
    surname2 = input("Dime tu segundo apellido: ")
    
    print("\nTus iniciales son")
    print(name[0], surname[0], surname2[0]) 

except:
    print("ERR0R")










