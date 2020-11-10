"""
Author: Manuel Brito
Program that read the age of peope and tell who is the youngest
"""

try:
    print("--Programa que te dice que persona es la más joven--\n")

    age1 = int(input("Dime la edad de la primera persona: "))
    age2 = int(input("Dime la edad de la segunda persona: "))
    
    if age1 < age2:
        print(f"El más joven es {age1}")
    elif age2 < age1:
        print(f"El más joven es {age2}")
    else:
        print("Tienen la misma edad")

except:
    print("ERROR")











