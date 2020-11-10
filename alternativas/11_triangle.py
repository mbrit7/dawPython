"""
Author: Manuel Brito
Program that with the sides of a triangle, show what type it's.
If follow Pythagoras is a right-angled triangle.
If two sides are equals is a isosceles triangle.
If all the sides are equals is a equilateral triangle.
If dont't have any of these condition is a scalene triangle.
"""

try:
    print("-- Programa que te dice el tipo de triángulo --")

    side1 = int(input("\nDime el valor de un lado: "))
    side2 = int(input("Dime el valor de otro lado: "))
    hipo = int(input("Dime el valor de hipotenusa: "))

    

    # Pythagoras's Theorem is when side1**2 + side2**2 = hipo**2
    if side1**2 + side2**2 == hipo**2:
        print("\n El triángulo introducido sigue el teorema de Pitágoras por lo que es rectángulo")
    elif side1 == side2:
        print("\nEl triángulo introducido es isósceles")
    elif side1 == side2 and side2 == hipo:
        print("\nEl triángulo es equilatero")
    else:
        print("\nEl triángulo es escaleno")


except:
    print("Err0r")










