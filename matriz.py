def creaMatriz2(n):
	matriz=[]
	for i in range(n):
		lista=[]
		for x in range(n):
			lista.append(i+1)
		matriz.append(lista)
	return matriz

def cuantaPares(lista_anidada):
	cont=0
	for lista in lista_anidada:
		for elem in lista:
			if elem%2==0:
				cont+=1
	return cont

def cuanto5(matriz):
	cont=0
	for lista in matriz:
		for elem in lista:
			if elem>5:
				cont+=elem
	return cont

def busca(lista_anidada,x):
	for lista in lista_anidada:
		if x in lista:
			return True
		else:
			return False


def cuentaPositivos(lista_anidada):
	cont=0
	for lista in matriz:
		for elem in lista:
			if elem>=0:
				cont+=1
	return cont