"""
Author: Manuel Brito
Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
"""
# Para calcular la hipotenusa del triángulo necesitas utilizar el teorema de Pitágoras
# c1^2 + c2^2 = h^2

import math

try:
    c1 = float(input("Dime el valor del primer cateto: "))
    c2 = float(input("Dime el valor del segundo cateto: "))
    h = math.sqrt(c1**2 + c2**2)
    print(f"La hipotenusa es = {h}")

except:
    print("ERR0R")

