"""
Author: Manuel Brito
Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
"""
print('---CONVERSIÓN A GRADOS CELSIUS---')

# Le pido al usuario el valor de la temperatura
n = float(input("\nDime un valor en grados Fahrenheit: "))

# Realizo los cálculos necesarios
celsius = round(((n - 32) / 1800), 2)

print(f"{n} grados Fahrenheit son {celsius} grados celsius")

