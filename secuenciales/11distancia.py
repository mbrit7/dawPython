"""
Author: Manuel Brito
Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
"""

try:
    n1 = float(input("Dime el valor del punto: "))
    n2 = float(input("Dime el valor del otro punto: "))
    
    print(f"La distancia entre {n1} y {n2} es de {round(abs(n1 - n2), 1)}")

except:
    print("ERR0R")







