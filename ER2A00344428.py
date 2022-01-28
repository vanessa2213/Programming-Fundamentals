def EstadoAgua(temp):
	if temp<-273:
		print("El agua tiene una temperatura existente.")
	elif -273<=temp<0 : 
		print("El agua se encuentra congelada.")
	elif 0<=temp<30 :
		print("El agua se encuentra fría.")
	elif 30<=temp<100:
		print("El agua se encuentra caliente.")
	else :
		print("El agua se encuentra en vapor.")
def esVocal(voc):
	if voc=="A" or voc=="E" or voc=="I" or voc=="O" or voc=="U":
		return True 
	elif voc=="a" or voc=="e" or voc=="i" or voc=="o" or voc=="u":
		return True
	else:
		return False
print("Programa con menú")
print("1. Programa estado del agua mediante temperatura.")
print("2. Vocal o no vocal.")


op=input("Teclea la opción deseada: ")
if op=="1":
	temp=int(input("Escribe la temperatura del agua: "))
	EstadoAgua(temp)
if op=="2":
	voc=input("Escribe un carácter: ")
	res=esVocal(voc)
	if res==True:
		print("Tu carácter {0} es una vocal.".format(voc))
	else :
		print("Tu carácter {0} no es una vocal.".format(voc))
