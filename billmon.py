print("Programa para convertir pesos en billetes y monedas")
p_billmil= 1000
p_bill_500=500
p_bill_200=200
p_bill_100=100
p_bill_50=50
p_bill_20=20
p_mon_10=10
p_mon_5=5
p_mon_1=1

pesos=int(input("Escribe la cantidad de pesos que deseas convertir: "))

billmil= pesos// p_billmil
pesos= pesos- (billmil*p_billmil)

bill500= pesos// p_bill_500
pesos= pesos - (bill500*p_bill_500)

bill200= pesos//p_bill_200
pesos= pesos-(p_bill_200*bill200)

bill100= pesos//p_bill_100
pesos= pesos-(p_bill_100*bill100)

bill50=pesos//p_bill_50
pesos= pesos-(bill50*p_bill_50)

bill20=pesos//p_bill_20
pesos= pesos- (bill20*p_bill_20)

mon10=pesos//p_mon_10
pesos= pesos-(mon10*p_mon_10)

mon5= pesos//p_mon_5
pesos= pesos-(mon5*p_mon_5)

mon1= pesos

print("{0:.0f} billetes de mil, {1:.0f} billetes de 500, {2:.0f} billetes de 200, {3:.0f} billetes de 100, {4:.0f} billetes de 50, {5:.0f} billetes de 20, {6:.0f} monedas de 10, {7:.0f} monedas de 5, {8:.0f} monedas de 1 .".format(billmil, bill500, bill200, bill100, bill50, bill20, mon10, mon5, mon1))