def multiplica3(n):
	if n==1:
		return 3
	else:
		return 3+multiplica3(n-1)
def exponencial3(n):
	if n==0:
		return 1
	else:
		return 3*exponencial3(n-1)
def factorial(x):
	if x==0:
		return 1
	else:
		return x*factorial(x-1)
def invierteLista(lista,inicio,fin):
	if inicio<fin:
		temp=lista[inicio]
		lista[inicio]=lista[fin]
		lista[fin]=temp
		invierteLista(lista,inicio+1,fin-1)
def enAscendente2(n):
	if n==0:
		print(0,end=" ")
	else:
		enAscendente2(n-1)
		print(n,end="")


