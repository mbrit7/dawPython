"""
Author: Manuel Brito
Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
"""

try:
# Le pido al usuario los datos necesarios
    com1 = float(input("Dime de cuanto es la primera comisión: "))
    com2 = float(input("Dime de cuanto es la segunda comisión: "))
    com3 = float(input("Dime de cuanto es la tercera comisión: "))
    sb = float(input("Dime cuanto cobras: "))
    
# Realizo las operaciones necesarias y muestro por pantalla
    sb += sb * 0.1
    print(f"Recibes un sueldo de {com1 + com2 + com3 + sb}")

except:
    print("ERR0R")










