def valida_entero(msg):
	while True:
		try:
			num=int(input(msg))
			return num
		except ValueError:
			print("Dato inválido, sólo valor numérico.")
def val_entero_pos(msg):
	num=input(msg)
	positivo=num.isdigit()
	while not positivo:
		print("Solo es permitido números enteros, ingresa de nuevo.")
		num=input(msg)
		positivo=num.isdigit()
	return int(num)
def no_vacio(msg):
	cadena=None
	while not cadena:
		cadena=input(msg)
	return cadena