def creaMatriz(n):
	matriz=[]
	for i in range(n):
		lista=[]
		for x in range(n):
			lista.append(i+1)
		matriz.append(lista)
	return matriz

def cuanto5(matriz):
	cont=0
	for lista in matriz:
		for elem in lista:
			if elem==5:
				cont+=1
	return cont

def cambiaCeros(matriz):
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if matriz[i][j]==0:
				matriz[i][j]=-1
n=int(input("Es:"))
print(creaMatriz(n))
