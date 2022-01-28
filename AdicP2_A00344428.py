def coincidenVocales(s1,s2):
	s1=s1.lower()
	s2=s2.lower()
	nue=""
	i=0
	while i<len(s1):
		pos=s2[i]
		i+=1
		while pos in s1:
			nue+=pos
	return re
def cuantosVacios(matriz):
	cont=0
	for lista in matriz:
		for elem in lista:
			if elem==0:
				cont+=1
	return cont
def aprobados(grupo):
	archivo=None
	try:
		archivo=open("calificaciones.csv")
	except:
		print("Error")
	if archivo:
 		for linea in archivo:
 			cadena=linea.rstrip()
 			if lista[0]==grupo:
 				cal1=float(lista[2])
 				cal2=float(lista[3])
 				cal3=float(lista[4])
 				calf=(cal1+cal2+cal3)/3
 				if calf>=70:
 					matr+=lista[1]+","
 		print(matr)
matriz=[0,0,1][0,1,1]
print(cuantosVacios(matriz))