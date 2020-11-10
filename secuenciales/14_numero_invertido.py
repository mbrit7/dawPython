"""
Author: Manuel Brito
Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
"""

try:
    n = int(input("Dime un número entero de dos cifras: "))

    # Para lograr separar los dígitos divido el número entre 10 para el primero
    # y el resto de 10 es el segundo dígito
    n1 = str(n // 10)
    n2 = str(n % 10)

    print(f"{n} invertido es {n2 + n1}")

except:
    print("ERROR")












