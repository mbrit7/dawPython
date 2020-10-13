"""
Author: Manuel Brito
Calcular el perimetro y área de un rectángulo dada su base y su altura.
"""

try:
    base = float(input("Dime la base del rectángulo: "))
    height = float(input("Dime la altura del rectángulo: "))
    perimeter = (base + height) * 2
    area = base * height
    print(f"El perímetro del rectángulo es = {perimeter} u")
    print(f"La base es igual a {area} u")
    
except:
    print("ERR0R")

