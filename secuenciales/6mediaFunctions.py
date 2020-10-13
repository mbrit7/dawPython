"""
Author: Manuel Brito
Voy a crear un programa que calcule la media de tres números introducidos
por el usuario utilizando el módulo statistics.
"""
import statistics as st

try:
    numbers = input("Dime tres números: ").split(" ")
    n = int[numbers] 
    print(st.mean(n))



except Exception as e:
    print(e)
    print("ERR0R")




