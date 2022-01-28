import random

print("Bienvenido!")
print("Piensa un número entre 0 y 100.")
print("Trataré de adivinarlo.")
print("Me tendrás que decir si es menor, mayor o igual al que te daré.")
print("Empecemos.")
mayor=100
menor=0
x=random.randint(menor,mayor)
res=input("¿Tu número es mayor, menor o igual a %d? "%(x))
res=res.lower()

while res!="igual":
	if res=="mayor":
		menor=x
		x=random.randint(menor,mayor)
		res=input("¿Tu número es mayor, menor o igual a %d? "%(x))
		res=res.lower()
	elif res=="menor":
		mayor=x
		x=random.randint(menor,mayor)
		res=input("¿Tu número es mayor, menor o igual a %d? "%(x))
		res=res.lower()
	else:
		print("Opción no valida intente de nuevo.")
		res=input()
print("Gracias por jugar conmigo!")