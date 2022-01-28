import random
def no_vacio(msg):
	cadena=None
	while not cadena:
		cadena=input(msg)
	return cadena
def valida_entero(msg):
	while True:
		try:
			num=int(input(msg))
			return num
		except ValueError:
			print("Dato inválido, sólo valor numérico.")
def tirada(n):
	contador=0
	for i in range(1,n+1):
		num=random.randint(1,6)
		contador+=num
		print("Número %d: %d"%(i,num))
	return contador
def revuelvePalabra(s):
	re=""
	i=0
	while i<len(s):
		pos=random.randint(0,(len(s)-1))
		re+=s[pos]
		i+=1
	return re	

def revuelvePalabra2(s):#mas eficiente
	re=""
	while s!="":
		pos=random.randint(0,(len(s)-1))
		re+=s[pos]
		s=s[:pos]+s[pos+1:]
	return re

def revuelvePalabra3(s):
	re=""
	lis=[]
	while len(lis)<len(s):
		pos=random.randint(0,len(s)-1)
		if not pos in lis:
			lis.append(pos)
			re+=palabra[pos]
	return rev

def menu():
	print("Selecciona una opción:")
	print("1. Tirada de dado n veces.")
	print("2. Revuelve palabra. ")
	print("3. Salir. ")
while True:
	menu()
	op=input("Inserta la opción que deseas: ")
	if op=="1":
		n=valida_entero("Ingresa un valor: ")
		con=tirada(n)
		print("Tu suma es de: %d"%(con))
	elif op=="2":
		s=input("Escribe: ")
		print(revuelvePalabra(s))
	elif op=="3":
		Exit()
	else:
		pint("El número que ingresaste no es valido.")
	



