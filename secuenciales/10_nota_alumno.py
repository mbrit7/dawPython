"""
Author = Manuel Brito
Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:

    * 55% del promedio de sus tres calificaciones parciales.

    * 30% de la calificación del examen final.

    * 15% de la calificación de un trabajo final.

"""
import statistics as st

try:
    # Le pido al usuario las calificaciones
    parcial1 = float(input("Dime la primera nota del parcial: "))
    parcial2 = float(input("Dime la segunda nota del parcial: "))
    parcial3 = float(input("Dime la tercera nota del parcial: "))
    final_exam = float(input("Dime la nota del examen final: "))
    final_work = float(input("Dime la nota del trabajo final: "))
    
    # Creo la lista 'mean' para poder utilizar el método mean 
    # y calcular la media directamente 
    mean = [parcial1, parcial2, parcial3] 
    
    # Realizo las operaciones y muestro los datos
    print(f"La nota de Algoritmos es {int(st.mean(mean) * 0.55) + int(0.30 * final_exam) + int(0.15 * final_work)}")

except:
    print("ERR0R")





