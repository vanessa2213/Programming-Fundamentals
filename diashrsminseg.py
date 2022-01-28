segdia = 86400
seghr = 3600
segmin = 60

segundos = int(input("Ingresa los segundos: "))

dias = segundos // segdia
segundos = segundos- (dias * segdia)

horas = segundos // seghr
segundos =segundos - (horas * seghr)

minutos = segundos // segmin
segundos = segundos - (minutos * segmin)

print("{0:.0f} dias, {1:.0f} horas, {2:.0f} minutos, {3:.0f} segundos.".format(dias, horas, minutos, segundos))