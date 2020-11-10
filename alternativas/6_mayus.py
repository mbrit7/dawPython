"""
Author: Manuel Brito
Program that read a string and check it's in uppercase
"""

try:
    print("--Programa que comprueba si una cadena está en mayúsculas--")

    string = input("\nDime una cadena: ")

    if len(string) > 1:
        print("Tienes que introducir una letra") 
    
    elif string.isupper() == True:
        print("La cadena introducida está en mayúsculas")

except:
    print("ERRor")











