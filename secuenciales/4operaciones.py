
"""
Author: Manuel Brito
Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
"""

try:
    print('--- Programa para calcular la suma, resta, multiplicación y división ---') 

    # Le pido al usuario dos números
    n1 = float(input("\nDime un número: "))
    n2 = float(input("Dime otro número: "))

    # Realizo las operaciones: suma, resta, multiplicación y división
    while n2 > n1:
        print("El segundo número tiene que ser menor, para realizar la resta")
        n3 = float(input("Dime otro número: "))
        n2 = n3 
    else:
        print(f"\nLa suma de {n1} y {n2} es = {n1 + n2}")
        print(f"La resta es = {n1 - n2}")
        print(f"La multiplicación es = {n1 * n2}")
      
   
except:
    print("ERR0R")
