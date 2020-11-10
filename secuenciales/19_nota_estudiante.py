"""
Author: Manuel Brito
Escribir un algoritmo para calcular la nota final de un estudiante, considerando que por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.
"""

try:
    print("El examen consta de diez preguntas")

    correctAns = int(input('\nCuantas preguntas tienes bien: '))
    incorrectAns = int(input('Dime cuantas preguntas tienes mal: '))
    noAns = int(input('Dime cuantas preguntas no has respondido: '))
   
    print(f'Tu nota del examen es {(correctAns * 5) + (incorrectAns * -1) + (noAns * 0)} sobre 50')

except:
    print('ERR0R')










