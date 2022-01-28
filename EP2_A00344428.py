def coincidencias(str1,str2):
	cont=0
	i=0
	while str1[i]:
		if str1[i] in str2:
			cont+=1
			i+=1
		else:
			i+=1
	return cont


def vacios(lista):
	lista1=""
	for pos in matriz:
		for elem in lista:
			if elem==1:
				lista1+=lista1.append(pos)
	return lista1

def valida_rango(msg,mini,maxi):
	while True:
		try:
			num=int(msg)
			try:
			  for num in range(mini,maxi):
			  	num=num
			except:
			  	print("El número que ingresaste no se encuentra entre los limites.")
		except ValueError:
			print("El dato que ingresaste no es un número.")

def minutos_usuario(stri):
	archivo=None
	try:
		archivo.open("log.csv")
	except:
		print("Error")
	if stri in archivo:
		for linea in archivo:
			cadena1=linea.strip("(")+linea.strip(")")
			minu=cadena1[7]
			hr=float(minu[:2])
			minu=float(minu[2:])
			minufin= minu+ (hr/60)
			print("Los minutos totales son:{0:.2f}".format(minufin))
			


		
