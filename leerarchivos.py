def cuadraticas(a,b.c):
	if a==0:
		if b==0:
			print("No es una ecuación.")
		else:
			x= -c/b
			print("X es igual a: {0:.3f}".format(x))
	else:
		if (b**2-4*a*c)<0:
			dis= math.sqrt(b**-4*a*c)
			ima= complex(0,math.sqrt(-dis))
			print("Solución imaginaria: {0:.2f}".format(ima))
		else:
			x1= (-b+math.sqrt(b**2-4*a*c))/(2*a)
			x2= (-b-math.sqrt(b**2-4*a*c))/(2*a)
			print("X1= {0:.3f}, X2= {1:.3f}.".format(x1,x2))


archivo=None
try:
	archivo=open("nombre.txt")
except:
	print("Error")
 if archivo:
 	for linea in archivo:
 		cadena=linea.rstrip()#quita los espacios de la derecha
 		lista=cadena.split(",") #entre lo que va a dividir en este caso coma
 		a=float(lista[0])
 		b=float(lista[1])
 		c=float(lista[2])
 		cuadratica(a,b,c)

