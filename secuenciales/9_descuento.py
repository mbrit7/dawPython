"""
Author: Manuel Brito
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra

"""

try:
# Le pido al usuario los datos necesarios
    price = float(input("¿Cuánto vale el producto?: "))

# Realizo las operaciones necesarias 
    price2 = price * 0.15
    realPrice = price - price2 
    print(f"El producto valía {price} y con el descuento vale {realPrice}") 

except:
    print("ERR0R")







