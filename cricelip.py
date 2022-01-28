print("Programa para calcular circunferencia de una elipse")
import math
a=float(input("Escriba el radio menor de la elipse: "))
b=float(input("Escriba el radio mayor de la elipse: "))

circ=2*math.pi*math.sqrt((math.pow(b,2)+math.pow(a,2))/2)

print("El perimetro de la elipse es {0:.3f}".format(circ))

