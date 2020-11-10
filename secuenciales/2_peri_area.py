"""
Author: Manuel Brito
Calcular el perimetro y área de un rectángulo dada su base y su altura.
"""

try:
    print('---Cálculo del perímetro y el área de un rectángulo---') 

    base = float(input("Dime la base del rectángulo: "))
    height = float(input("Dime la altura del rectángulo: "))
    perimeter = (base + height) * 2
    area = base * height
    
    print(f"\nEl perímetro del rectángulo es = {perimeter} u")
    print(f"La base es igual a {area} u")
    
except:
    print("ERR0R")

