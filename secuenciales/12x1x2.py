"""
Author: Manuel Brito
Pide al usuario dos pares de números x1,y1 y x2,y2 que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.
"""

# Para calcular la distancia entre dos puntos en el plano es necesario 
# utilizar la siguiente fórmula sqrt((x2 - y2)**2 + (x1 - x2)**2))

from math import sqrt

try:
    x1 = int(input("Dime el valor de x1: "))
    y1 = int(input("Dime el valor de y1: "))
    x2 = int(input("Dime el valor de x2: "))
    y2 = int(input("Dime el valor de y2: "))

    print(f"La distancia entre {x1, y1} y {x2, y2} es de {round(sqrt((x2 - y2)**2 + (x1 - y1)**2), 1)}")

except:
    print("ERR0R")







