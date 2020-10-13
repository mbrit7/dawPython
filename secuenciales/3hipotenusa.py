"""
Author: Manuel Brito
Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
"""

# Para calcular la hipotenusa del triángulo necesitas utilizar el teorema de Pitágoras
# c1^2 + c2^2 = h^2

from math import sqrt 

try:
    print('>>> Programa que calcula la hipotenusa de triángulo rectángulo <<<') 

    side1 = float(input("\nDime el valor del primer cateto: "))
    side2 = float(input("Dime el valor del segundo cateto: "))
    h = int(sqrt(side1 ** 2 + side2 ** 2))
    print(f"\nLa hipotenusa es = {h}")

except:
    print("ERR0R")

