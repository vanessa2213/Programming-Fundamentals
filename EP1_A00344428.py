import math
def funcion_intervalos(x):
	fun2= math.pow(x,2)-4
	fun3= math.pow(x,2)-(2*x)+32
	if x<=-2:
		res= x+3
		return res
	elif -2<x<3:
		return fun2
	else:
		return fun3
def huracanes(marea):
	me_pi= .0254
	marea1= marea/me_pi
	if 4<=marea1<6:
		print("El huracán es de categoría 1 y de un daño mínimo.")
	elif 6<=marea1<9:
		print("El huracán es de categoría 2 y de un daño moderado.")
	elif 9<=marea1<13:
		print("El huracán es de categoría 3 y de un daño extenso.")
	elif 13<=marea<19:
		print("El huracán es de categoría 4 y de un daño extremo.")
	elif marea1>=19 :
		print("El huracán es de categoría 5 y de un daño catastrófico.")
	else:
		print("No es un huracán.")
def encripta(palabra):
	palabra=palabra.lower()
	palabra=palabra.replace("a","*")
	palabra=palabra.replace("e","3")
	palabra=palabra.replace("i","=")
	palabra=palabra.replace("o","@")
	palabra=palabra.replace("u",">")
	return palabra
def mas_larga(cadena1,cadena2):
	count1=len(cadena1)
	count2=len(cadena2)
	if count1>count2:
		return 1
	elif count2>count1:
		return -1
	else
		return 0

print("Programa con menú")
print("1. Funciones.")
print("2. Huracanes.")
print("3. Encripta.")
print("4. Cadena mas larga.") 

op=input("Teclea la opción deseada: ")
if op=="1":
	x=float(input("Escribe el valor de x: "))
	res=funcion_intervalos(x)
	print("Tu resultado es {0:.2f}.".format(res))
elif op=="2":
	marea=int(input("Escribe la marea de la tormenta."))
	huracanes(marea)
elif op=="3":
	cadena=input("Escibe tu frase: ")
	print(encripta(cadena))
elif op=="4":
	cadena1=input("Escribe tu primera frase: ")
	cadena2=input("Escribe tu segunda frase: ")
	res=mas_larga(cadena1,cadena2)
	if res==1:
		print("Tu primera cadena es más larga que la segunda.")
	elif res==0:
		print("Tus cadenas tienen la misma longitud.")
	else:
		print("Tu segunda cadena es más larga que la segunda.")
else:
	print("Error.")