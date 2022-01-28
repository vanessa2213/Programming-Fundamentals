print("Programa para calcular largo de una escalera")
import math
al=float(input("Escribe la altura: "))
an=float(input("Escribe el ángulo: "))

largo= al/math.sin(an)

print("El largo de la escalera es: {0:.2f}".format(largo))