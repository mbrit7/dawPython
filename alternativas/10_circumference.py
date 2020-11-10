"""
Author: Manuel Brito
Program that with the central points x1, y1, x2, y2 and radius r1 and r2 of two circumferences.
Clasify it's by:
    -outer
    -outer tangent
    -secant
    -inner tangent
    -inner
    -concentric
"""

from math import sqrt 

try:
    x1 = int(input("Dime el valor de x1: "))
    y1 = int(input("Dime el valor de x2: "))
    r1 = int(input("Dime el valor de r1: "))

    x2 = int(input("\nDime el valor de x2: "))
    y2 = int(input("Dime el valor de y2: "))
    r2 = int(input("Dime el valor de r2: "))
    
    # For some calcs I need the distance between centers
    # distance_centers = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    distance_centers = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    print(distance_centers)
    # A circumference is outer when the distance between centers is greater than the
    # addition of radius
    if distance_centers > (r1 + r2):
        print("\n La circunferencia es exterior")

except:
    print("Err0r")







