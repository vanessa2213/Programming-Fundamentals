import datetime
import time
from datetime import date 
import os 

archivo=None
archivo1=None
registro=0
respuestaderegreso="si"
fechanew= str(date.today())

def ver_entero_pos(msg):
	while True:
		num=input(msg)
		if num.isdigit():
			return num
		else:
			print("Solo se permiten numeros enteros positivos:")

def siguiente_dia(fecha,n):
	lifecha = fecha.split("-")
	fecha = datetime.date(int(lifecha[0]),int(lifecha[1]),int(lifecha[2]))
	sigfecha = fecha+datetime.timedelta(days=n)
	return sigfecha

def valida_opciones(x,y,msg):
	respuesta = (input(msg))
	while respuesta != x and respuesta != y:
		print("Respuesta incorrecta, solo se permite {0} o {1} por favor intente de nuevo".format(x,y))
		respuesta = input(msg)
	return respuesta 

def ver_op_num(x,y,msg):
	resp = int(input(msg))
	while resp<x or resp>y:
		print("Dato incorrecto, ingresa una opcion valida que se encuentre entre {0} y {1}.".format(x,y))
		resp = int(input(msg))
	return resp

def menu():
	print(time.strftime("%H:%M:%S"))
	print("Compañia CLE.")
	print("Menú: ")
	print("Selecciona una opción:")
	print("1. Ingresar datos.")
	print("2. Reporte.")
	print("3. Reiniciar Semana.")
	print("4. Consultar linea de producción.")
	print("5. Salir.")

def Ingresardatos(fecha):
	try:
		archivo=open("Vane.txt","a+",encoding="UTF-8")
	except IOError:
		print("El archivo no fue encontrado.")
	if archivo:
		print(fecha)
		for turno in range(1,4):
			for linea in range(1,6):
				print("Turno {0}, Linea {1}, {2}".format(turno,linea,fecha))
				Linea="Linea"+str(linea)
				Turno="Turno"+str(turno)
				productos=ver_entero_pos("Ingresa los productos que fueron elaborado en la linea {0} turno {1}: ".format(linea,turno))
				veces=ver_entero_pos("¿Cuántas veces fue detenida la linea? ")
				lineafin = Linea,Turno,fecha,productos,veces
				archivo.write((str(Linea)+","+str(Turno)+","+str(fecha)+","+str(productos)+","+str(veces)+"\n"))
				print("*************************************************************************************")
	return ""
	archivo.close()

def resumen(linea_prod,turno):
	try:
		archivo = open("Vane.txt","r",encoding = "UTF-8")
	except IOError:
		print("El archivo no fue encontrado.")
	if archivo:
		productos = 0
		veces = []
		detenidas = []
		dia_menos = ""
		linea1 = ""
		turno1 = ""
		variable = 0
		for linea in archivo: 
			cadena = linea.strip()
			lista = cadena.split(",")
			if lista[0]== linea_prod:
				if lista[1]== turno:
					linea1 = str(lista[0])
					turno1 = str(lista[1])
					productos= productos + int(lista[3])
					veces.append(int(lista[4]))
					variable = variable + int(lista[4]) 
					detenidas.append(lista[2])
					mayor = max(veces)
					dias_mas = veces.index(mayor)
					c = 0
					while veces[c]!= mayor:
						c = c + 1
					dia_menos = detenidas[c]	
	try:
		archivo1 = open("VaneRes.txt","a+",encoding = "UTF-8")
	except IOError:
		print("El archivo no fue encontrado.")
	if archivo1:
		print("Linea:"+str(linea1)+"\n")
		print("Turno:"+str(turno1)+"\n")
		print("Total de productos:"+str(productos)+"\n")
		print("Veces que se detuvo la linea:"+str(variable)+"\n")
		print("El dia que mas se detuvo fue:"+str(dia_menos)+"\n")
		archivo1.write("Linea:"+str(linea1)+"\n")
		archivo1.write("Turno:"+str(turno1)+"\n")
		archivo1.write("Total de productos:"+str(productos)+"\n")
		archivo1.write("Veces que se detuvo la linea:"+str(variable)+"\n")
		archivo1.write("El dia que mas se detuvo fue:"+str(dia_menos)+"\n")
	return ""
	archivo.close()
	archivo1.close()	

def reiniciarsemana(fecha):
	repo=input("¿Quieres generar un reporte? ")
	if repo=="si":
		try:
			archivo1 = open("VaneRes.txt","w+",encoding = "UTF-8")
		except IOError:
			print("No se puede abrir o no existe el archivo")
		if archivo1:
			archivo1.write("")
		archivo1.close()	
		resumen("Linea1","Turno1")
		resumen("Linea1","Turno2")
		resumen("Linea1","Turno3")
		resumen("Linea2","Turno1")
		resumen("Linea2","Turno2")
		resumen("Linea2","Turno3")
		resumen("Linea3","Turno1")
		resumen("Linea3","Turno2")
		resumen("Linea3","Turno3")
		resumen("Linea4","Turno1")
		resumen("Linea4","Turno2")
		resumen("Linea4","Turno3")
		resumen("Linea5","Turno1")
		resumen("Linea5","Turno2")
		resumen("Linea5","Turno3")
		print("Se creo satisfactoriamente el resumén. Para consultarlo habre el archivo VaneRes.txt ")
	elif repo=="no":
		while True:
			try:
				archivo=open("Vane.txt","w+",encoding="UTF-8")
			except IOError:
				print("El archivo no fue encontrado")
			if archivo:
				fechafinal = siguientedia(fecha,7)
				file.write("Semana del"+str(fecha)+"al"+str(fechafinal))
				file.close()
	else:
		print("La opcion ingresada no es valida, prueba con un si o un no.")


while respuestaderegreso=="si":
	menu()
	op=input("Inserta la opción que deseas: ")
	if op=="1":
		if registro==0:
			Ingresardatos(siguiente_dia(fechanew,0))
			print("Los datos del dia de hoy fueron ingresados correctamente, gracias. ")
			registro=+1
			respuestaderegreso=valida_opciones("si","no","¿Desea regresar al menú principal? <si-no> ")
		elif registro==1:
			Ingresardatos(siguiente_dia(fechanew,1))
			print("Los datos del dia de hoy fueron ingresados correctamente, gracias. ")
			registro=+2
			respuestaderegreso=valida_opciones("si","no","¿Desea regresar al menú principal? <si-no> ")
		elif registro==2:
			Ingresardatos(siguiente_dia(fechanew,2))
			print("Los datos del dia de hoy fueron ingresados correctamente, gracias. ")
			registro=+3
			respuestaderegreso=valida_opciones("si","no","¿Desea regresar al menú principal? <si-no> ")
		elif registro==3:
			Ingresardatos(siguiente_dia(fechanew,3))
			print("Los datos del dia de hoy fueron ingresados correctamente, gracias. ")
			registro=+4
			respuestaderegreso=valida_opciones("si","no","¿Desea regresar al menú principal? <si-no> ")
		elif registro==4:
			Ingresardatos(siguiente_dia(fechanew,4))
			print("Los datos del dia de hoy fueron ingresados correctamente, gracias. ")
			registro=+5
			respuestaderegreso=valida_opciones("si","no","¿Desea regresar al menú principal? <si-no> ")
		elif registro==5:
			Ingresardatos(siguiente_dia(fechanew,5))
			print("Los datos del dia de hoy fueron ingresados correctamente, gracias. ")
			registro=+6
			respuestaderegreso=valida_opciones("si","no","¿Desea regresar al menú principal? <si-no> ")
		elif registro==6:
			Ingresardatos(siguiente_dia(fechanew,6))
			print("Los datos del dia de hoy fueron ingresados correctamente, gracias. ")
			respuestaderegreso=valida_opciones("si","no","¿Desea regresar al menú principal? <si-no> ")
			registro=+7
		else:
			print("Terminaste de ingresar todos los datos de esta semana.")
			respuestaderegreso=valida_opciones("si","no","¿Deseas regresar al menú principal?" )
	elif op=="2":
		try:
			archivo1 = open("VaneRes.txt","w+",encoding = "UTF-8")
		except IOError:
			print("No se puede abrir o no existe el archivo")
		if archivo1:
			archivo1.write("")
		archivo1.close()	
		resumen("Linea1","Turno1")
		resumen("Linea1","Turno2")
		resumen("Linea1","Turno3")
		resumen("Linea2","Turno1")
		resumen("Linea2","Turno2")
		resumen("Linea2","Turno3")
		resumen("Linea3","Turno1")
		resumen("Linea3","Turno2")
		resumen("Linea3","Turno3")
		resumen("Linea4","Turno1")
		resumen("Linea4","Turno2")
		resumen("Linea4","Turno3")
		resumen("Linea5","Turno1")
		resumen("Linea5","Turno2")
		resumen("Linea5","Turno3")
		print("Se creo satisfactoriamente el resumén. Para consultarlo habre el archivo VaneRes.txt ")
		respuestaderegreso=valida_opciones("si","no","¿Deseas regresar al menú principal?")
	elif op=="3":
		if registro>6:
			fechanew = input("Ingresa la primer fecha de la siguiente semana:(En el siguiente formato:2017-10-20"+"\n")
			reiniciarsemana(fechanew)
			print("Listo, se ha reiniciado la semana, puede dirigirse a la opcion 1 del")
			print("menu principal para empezar a ingresar nuevos datos")
			registro = 0
			respuestaderegreso = valida_opciones("si","no","¿Desea regresar al menu principal? <si-no>")
		else:
			print("Lo siento no puedes reiniciar la semana hasta terminar de registrar los datos de toda la semana.")

	elif op=="4":
		l= "Linea"+ str(ver_op_num(1,5,"Ingresa el numero de la linea que desees:"))
		t= "Turno"+str(ver_op_num(1,3,"Ingresa el numero de el turno que desees:"))
		try:
			archivo1 = open("VaneRes.txt","a+",encoding = "UTF-8")
		except IOError:
			print("No se puede abrir o no existe el archivo")
		if archivo1:
			archivo1.write("")
		archivo1.close()	
		resumen(l,t)
		print("Se creo tu resumen parcial,para verlo abre el archivo")
		respuestaderegreso = valida_opciones("si","no","¿Desea regresar al menu principal? ")
	elif op=="5":
		print("Hasta luego!")
		exit()
	else:
		print("La opción que ingresaste no es valida, intenta de nuevo.")
print("Hasta luego!")

