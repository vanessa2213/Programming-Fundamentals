def num_dig(n):
	count=1
	i=10
	while i<=n:
		count+=1
		i=i*10
	print("La cantidad de dígitos por las que esta compuesto %d es: %d."%(n,count))

n=int(input("Escribe el número: "))
num_dig(n)
