def esVocal(caracter):
	return caracter in "aeiouAEIOU"
def cuantasVoc(cadena):
	cadena=cadena.lower()
	return cadena.count("a")+cadena.count("e")+cadena.count("i")+cadena.count("o")+cadena.count("u")
def suprimeVoc(palabra):
	palabra=palabra.lower()
	palabra=palabra.replace("a","")
	palabra=palabra.replace("e","")
	palabra=palabra.replace("i","")
	palabra=palabra.replace("o","")
	palabra=palabra.replace("u","")
	return palabra
def palindrome(string):
	string=string.lower()
	string=string.replace(' ',"")
	al=string[::-1]
	if al==string:
		return True
	else:
		return False
print("Programa con menú")
print("1. Es vocal.")
print("2. Cuantas vocales.")
print("3. Suprime Vocales")
print("4. Palindrome.") 

op=input("Teclea la opción deseada: ")
if op=="1":
	voc=input("Escribe un carácter: ")
	res=esVocal(voc)
	if res==True:
		print("Tu carácter {0} es una vocal.".format(voc))
	else :
		print("Tu carácter {0} no es una vocal.".format(voc))
if op=="2":
	st=input("Teclea palabra o frase: ")
	num=cuantasVoc(st)
	print("Tu string tiene {0} vocales.".format(num))
if op=="3":
	st=input("Teclea palabra o frase: ")
	print(suprimeVoc(st))
if op=="4":
	st=input("Teclea una frase o una palabra: ")
	res=palindrome(st)
	if res==True:
		print("Si es un palindrome.")
	else:
		print("No es un palindrome.")