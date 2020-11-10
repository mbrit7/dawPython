"""
Author: Manuel Brito
Program that show 'ACEPTADA' if the mark is greater or equal than five, the age is greater or equal than
eighteen and the genre is 'F'. Also if the mark and age are the same but the genre is 'M', show 'POSIBLE'
However, if the any condition is accepted show 'NO ACEPTADA'.
The data are 'mark', 'age' and 'genre'.
"""

try:
    print("--- Programa que acepta a personas ---\n") 

    mark = int(input("Dime tu nota sobre diez: "))
    age = int(input("Dime tu edad: "))
    genre = input("Dime tu género(F o M): ")

    if mark >= 5 and age >= 18 and genre == "F":
        print("\nACEPTADA")
    elif mark >= 5 and age >= 18 and genre == "M":
        print("\nPOSIBLE") 
    else:
        print("\nNO ACEPTADA")

except:
    print("ErrOr")













