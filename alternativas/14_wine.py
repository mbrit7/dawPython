"""
Author: Manuel Brito
Program that show the earnings of a wine business
"""

try:
    print(">>> Programa que muestra las ganancias de una viticultora <<<\n")
    
    # I order to the user to introduce the inicial price of the grape and the kgs of grapes
    # the type and the size

    inicial_price = float(input("Dime el precio inicial en céntimos: "))
    kg = int(input("Dime los kilogramos de uvas: "))
    type_grape = input("Dime el tipo de la uva(A o B): ")
    size_grape = input("Dime que tamaño es (1 o 2): ")
    
    if (type_grape == "A" and size_grape == "1"):
        inicial_price += 0.20
    elif (type_grape == "A" and size_grape == "2"):
        inicial_price += 0.30
    elif (type_grape == "B" and size_grape == "1"):
        inicial_price += 0.20
    elif (type_grape == "B" and size_grape == "2"):
        inicial_price += 0.30
    
    print(f"\nLas ganancias son de {(inicial_price * kg)/100} euros")

except:
    print("Err0r")





