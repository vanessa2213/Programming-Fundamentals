import random
print("Bienvenido!")
print("Pensaré un número entre el 0 y el 100.")
print("Tu tratarás de adivinarlo, pero solo tendrás 5 intentos")
print("Yo te diré si es menor mayor o igual al número que tu me des.")
print("Empecemos.")
x=random.randint(0,100)
i=0
while i!=5:
	res=int(input("Escribe el número que piensas que es: "))
	if res!=x:
		if res>x:
			print("Mi número es menor a %d."%(res))
			i+=1
		elif res<x:
			print("Mi número es mayor a %d."%(res))
			i+=1
		else:
			print("Opción no valida intente de nuevo.")
			res=input()
	else:
		print("Adivinaste el número!")
		i=5
print("Gracias por jugar conmigo!")
