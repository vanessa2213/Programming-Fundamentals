r1=int(input("Primera resistencia: "))
r2=int(input("Segunda resistencia: "))
r3=int(input("Tercera resistencia: "))

rfinal= 1/(1/r1 + 1/r2 + 1/r3)

print("{0:.0f} ohms.".format(rfinal))