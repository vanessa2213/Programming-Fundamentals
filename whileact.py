def validación_enteros(msg):
	while True:
		try:
			num=int(input(msg))
			break
		except ValueError:
			print("Valor no válido, solo enteros, intentalo de nuevo.")
	return num
def f2(n):
	i=1
	con=0
	while i<=n:
		con+=i
		i+=1
	return con 

def f1(n):
	con=1
	i=1
	while i<=n:
		con=con*2*i
		i+=1
	return con

def h1(n):
	con=0
	i=0
	while i<=n:
		if i%2==0:
			con-=i
		else:
			con+=i
		i+=1
	return con

def h2(n):
	con=0
	i=0
	while i<=n:
		con+=((2*i)+2)
		i+=1
	return con

def numeros_triangulares(n):
	i=1
	t=0
	while i<=n:
		t=i*(i+1)/2
		print("T%d de %d = %d"%(i,n,t))
		i+=1

def num_dig(n):
	count=1
	i=10
	while i<=n:
		count+=1
		i=i*10
	print("La cantidad de dígitos por las que esta compuesto %d es: %d."%(n,count))



print("Programa con menú")
print("1. Serie.")
print("2. Serie 2n.")
print("3. Serie más ménos.")
print("4. Suma 2n + 2")
print("5. Escribe n y te da lo n números triangulares.")
print("6. Cantidad de dígitos de un número.")
op=input("Teclea la opción deseada: ")

if op=="1":
	msg="Teclea el hasta el número que quieres llegar tu serie."
	n=int(validación_enteros(msg))
	num=f2(n)
	print("El resultado de la suma de tus números hasta el %d es: %d."%(n,num))
elif op=="2":
	msg="Teclea un valor para n: "
	n=validación_enteros(msg)
	num=f1(n)
	print("El resultado de tu serie 2*%d es: %d"%(n,num))
elif op=="3":
	msg="Escribe hasta cuál número quieres llegar: "
	n=validación_enteros(msg)
	num=h1(n)
	print("El resultado de tu serie más ménos hasta el número %d es: %d"%(n,num))
elif op=="4":
	msg="Escribe un valor para n: "
	n=validación_enteros(msg)
	num=h2(n)
	print("El resultado de la seria 2 * %d + 2= %d."%(n,num))
elif op=="5":
	msg="Teclea tu número n: "
	n=validación_enteros(msg)
	numeros_triangulares(n)
elif op=="6":
	msg="Escribe tú número: "
	n=validación_enteros(msg)
	num_dig(n)
else:
	print("El %s que ingresaste no se encuentra en el menú"%(op))


