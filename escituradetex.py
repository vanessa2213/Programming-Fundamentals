import datetime
import time
from datetime import date 
import os 

def escribir(n):
	file = None
	try:
		file = open("Ric.txt","a+",encoding = "UTF-8")
	except IOError:
		print("No se puede abrir o no existe el archivo")
	if file:
		fecha = n
		print(fecha)
		for turno in range(1,4):
			for linea in range(1,6):
				print("Linea",linea,",turno",turno,)
				Linea = "Linea"+ str(linea)
				Turno = "Turno"+ str(turno)
				productos = valida_enteroypositivo("Ingresa el numero de productos elaborados:")
				detenidas = valida_enteroypositivo("ingresa el numero de veces que se detuvo la linea:")
				lineadetxt = Linea,Turno,fecha,productos,detenidas,
				file.write((str(Linea)+","+str(Turno)+","+str(fecha)+","+str(productos)+","+str(detenidas)+"\n"))
				print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
								

	return ""
	file.close()		


def crearesumen(lineapro,turno):
	file = None
	try:
		file = open("Ric.txt","r",encoding = "UTF-8")
	except IOError:
		print("No se puede abrir o no existe el archivo")

	if file:
		totaldeproducto = 0
		vecesquesedetuvo = []
		detenidas = []
		diafatal = ""
		linea1 = ""
		turno1 = ""
		variable = 0
		for linea in file: 
			cadena = linea.strip()
			lista = cadena.split(",")
			if lista[0]== lineapro:
				if lista[1]== turno:
					linea1 = str(lista[0])
					turno1 = str(lista[1])
					totaldeproducto = totaldeproducto + int(lista[3])
					vecesquesedetuvo.append(int(lista[4]))
					variable = variable + int(lista[4]) 
					detenidas.append(lista[2])
					mayor = max(vecesquesedetuvo)
					diasquemassedetuvo = vecesquesedetuvo.index(mayor)
					c = 0
					while vecesquesedetuvo[c]!= mayor:
						c = c + 1
					diafatal = detenidas[c]	
			
	archivo = None
	try:
		archivo = open("Resumen.txt","a+",encoding = "UTF-8")
	except IOError:
		print("No se puede abrir o no existe el archivo")
	if archivo:
		print("Linea:"+str(linea1)+"\n")
		print("Turno:"+str(turno1)+"\n")
		print("Total de productos:"+str(totaldeproducto)+"\n")
		print("Veces que se detuvo la linea:"+str(variable)+"\n")
		print("El dia que mas se detuvo fue:"+str(diafatal)+"\n")
		archivo.write("Linea:"+str(linea1)+"\n")
		archivo.write("Turno:"+str(turno1)+"\n")
		archivo.write("Total de productos:"+str(totaldeproducto)+"\n")
		archivo.write("Veces que se detuvo la linea:"+str(variable)+"\n")
		archivo.write("El dia que mas se detuvo fue:"+str(diafatal)+"\n")
	return ""
	archivo.close()
	file.close()	



																						
def reiniciar(fecha):
	file = None
	try:
		file = open("Ric.txt","w+",encoding="UTF-8")
	except IOError:
		print("No se puede abrir el archivo o el archivo no existe")
	if file:
		fechafinal = siguientedia(fecha,7)
		file.write("Semana del"+"" +str(fecha)+""+"al"+""+str(fechafinal)+"\n")
	file.close()
	


def valida_opciones_num(x,y,msg):
	respuesta = int(input(msg))
	while respuesta <x or respuesta >y:
		print("Dato incorrecto, ingresa una opcion valida")
		respuesta = int(input(msg))
	return respuesta
def valida_opciones(x,y,msg):
	respuesta = (input(msg))
	while respuesta != x and respuesta != y:
		print("Respuesta incorrecta por favor intente de nuevo")
		respuesta = (input(msg))
	return respuesta 

def valida_entero(msg):
	while True:
		try:
			num = int(input(msg))
			return num 
		except ValueError:
			print("Dato incorrecto,solo numeros enteros")

def valida_enteroyeleccion(x,y,msg):
	num = valida_entero((msg)) 		
	while num <x or num >y:
		print("Dato incorrecto por favor ingresa una opcion valida")
		num = int(input(msg))
	return num 
def valida_enteroypositivo(msg):
	num = valida_entero(msg)
	positivo = str(num).isdigit()
	while not positivo:
		print("Solo es permitido ingresar numeros positivos")
		num = input(msg)
		positivo = str(num).isdigit()
	return num			


def val_entero_pos(msg):
	num = input(msg)
	positivo = num.isdigit()
	while not positivo:
		print("Solo es permitido ingresar numeros positivos")
		num = input(msg)
		positivo = num.isdigit()
	return num
def siguientedia(strfecha,n):
	lifecha = strfecha.split("-")
	fecha = datetime.date(int(lifecha[0]),int(lifecha[1]),int(lifecha[2]))
	sigfecha = fecha+datetime.timedelta(days=n)
	return (sigfecha)



registro = 0
respuestaderegreso = "si"
fechanew= str(date.today())
while respuestaderegreso == "si":
	print("XETU.Inc")
	print("Computadora central de registro de produccion de lineas")
	print(time.strftime("%H:%M:%S")+"\n")
	print("")
	print("")
	print("")
	print("Menu")
	print("1.Ingresar datos de la linea")
	print("2.Resumen")
	print("3.Reiniciar datos de la semana")
	print("4.Consultas parciales")
	print("5.Salir")
	opcion = valida_enteroyeleccion(1,5,"Ingresa el numero de la opcion que desees:")
	if opcion == 1:	
		if registro == 0:
			file = None
			try:
				file = open("Ric.txt","w+",encoding = "UTF-8")
			except IOError:
				print("No se puede abrir o no existe el archivo")
			if file:
				file.write("")
			file.close()
			escribir(siguientedia(fechanew,0))
			print("Terminaste con los datos del dia de hoy,gracias")
			registro = registro + 1
			respuestaderegreso = valida_opciones("si","no","¿Desea regresar al menu principal? <si-no>")
		elif registro == 1:
			escribir(siguientedia(fechanew,1))
			print("Terminaste con los datos del dia de hoy,gracias")
			registro = registro + 1
			respuestaderegreso = valida_opciones("si","no","¿Desea regresar al menu principal? <si-no>")
		elif registro == 2:
			escribir(siguientedia(fechanew,2))
			print("Terminaste con los datos del dia de hoy,gracias")
			registro = registro + 1
			respuestaderegreso = valida_opciones("si","no","¿Desea regresar al menu principal? <si-no>")
		elif registro == 3:
			escribir(siguientedia(fechanew,3))
			print("Terminaste con los datos del dia de hoy,gracias")
			registro = registro + 1
			respuestaderegreso = valida_opciones("si","no","¿Desea regresar al menu principal? <si-no>")
		
		elif registro == 4:
			escribir(siguientedia(fechanew,4))
			print("Terminaste con los datos del dia de hoy,gracias")
			registro = registro + 1
			respuestaderegreso = valida_opciones("si","no","¿Desea regresar al menu principal? <si-no>")
		
		elif registro == 5:
			escribir(siguientedia(fechanew,5))
			print("Terminaste con los datos del dia de hoy,gracias")
			registro = registro + 1
			respuestaderegreso = valida_opciones("si","no","¿Desea regresar al menu principal? <si-no>")
		
		elif registro == 6:	
			escribir(siguientedia(fechanew,6))
			print("Terminaste con el registro de la semana,gracias")
			registro = registro + 1
			respuestaderegreso = valida_opciones("si","no","¿Desea regresar al menu principal? <si-no>")
		
		else:
			print("Lo siento ya no puedes ingresar mas datos, completaste la semana")
			respuestaderegreso = valida_opciones("si","no","¿Desea regresar al menu principal? <si-no>")
	
	elif opcion == 2:
		archivo = None
		try:
			archivo = open("Resumen.txt","w+",encoding = "UTF-8")
		except IOError:
			print("No se puede abrir o no existe el archivo")
		if archivo:
			archivo.write("")
		archivo.close()	
		crearesumen("Linea1","Turno1")
		crearesumen("Linea1","Turno2")
		crearesumen("Linea1","Turno3")
		crearesumen("Linea2","Turno1")
		crearesumen("Linea2","Turno2")
		crearesumen("Linea2","Turno3")
		crearesumen("Linea3","Turno1")
		crearesumen("Linea3","Turno2")
		crearesumen("Linea3","Turno3")
		crearesumen("Linea4","Turno1")
		crearesumen("Linea4","Turno2")
		crearesumen("Linea4","Turno3")
		crearesumen("Linea5","Turno1")
		crearesumen("Linea5","Turno2")
		crearesumen("Linea5","Turno3")
		
		print("Se creo el resumen de la semana, para verlo abre el archivo de texto")
		respuestaderegreso = valida_opciones("si","no","¿Desea regresar al menu principal? <si-no>")
	elif opcion == 3:
		if registro > 6:
			fechanew = input("Ingresa la primer fecha de la siguiente semana:(En el siguiente formato:2017-10-20"+"\n")
			reiniciar(fechanew)
			print("Listo, se ha reiniciado la semana, puede dirigirse a la opcion 1 del")
			print("menu principal para empezar a ingresar nuevos datos")
			registro = 0
			respuestaderegreso = valida_opciones("si","no","¿Desea regresar al menu principal? <si-no>")

		else:
			print("Lo siento no puedes reiniciar la semana hasta terminar de registrar los datos")
				
	elif opcion == 4:
		linea = "Linea"+ str(valida_opciones_num(1,5,"Ingresa el numero de la linea que desees:"))
	
		turno = "Turno"+str(valida_opciones_num(1,3,"Ingresa el numero de el turno que desees:"))
		print("Se creo tu resumen parcial,para verlo abre el archivo")
		archivo = None
		try:
			archivo = open("Resumen.txt","a+",encoding = "UTF-8")
		except IOError:
			print("No se puede abrir o no existe el archivo")
		if archivo:
			archivo.write("")
		archivo.close()	
		crearesumen(linea,turno)
		respuestaderegreso = valida_opciones("si","no","¿Desea regresar al menu principal? <si-no>")


	else:
		break
print("Gracias, que tenga un gran dia")					