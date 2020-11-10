"""
Author: Manuel Brito
Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?
"""

# Según las propiedades de las operaciones una raíz cuadrada se puede realizar multiplicando
# el número a averiguar por uno partido de el índice de la raíz
# sqrt(4) = 4 * (1 / 2)

try:
    n = int(input("Dime un número entero: "))

    print(f"La raíz cuadrada de {n} es {n * (1//2)}")
    print(f"La raíz cúbica de {n} es {n * (1//3)}")

except:
    print("ERR0R")








