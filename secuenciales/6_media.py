"""
Author: Manuel Brito
Calcular la media de tres números pedidos por teclado.
"""

try:
    print('---CÁLCULO DE LA MEDIA DE TRES NÚMEROS---') 

    n1 = float(input("Dime un número: ")) 
    n2 = float(input("Dime un número: ")) 
    n3 = float(input("Dime un número: ")) 
    
    # La media se calcula sumando los números entre la cantidad de estos
    print(f"\nLa media es igual a {int((n1 + n2 + n3) // 3)}")
except:
    print("ERR0R")




