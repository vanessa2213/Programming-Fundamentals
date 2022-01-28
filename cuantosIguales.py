x=int(input("Escribe tú primer número: "))
y=int(input("Escribe tú segundo número: "))
z=int(input("Escribe tú tercer número: "))

if x==y :
	if y==z:
		print("Los tres números son iguales.")
	else :
		print("Dos números son iguales.")
elif x==z:
	if z==y:
		print("Los tres números son iguales.")
	else:
		print("Dos números son iguales.")
elif y==z:
	if z==x:
		print("Los tres números son iguales.")
	else:
		print("Dos números son iguales.")
else:
	print("Los tres números son diferentes.")