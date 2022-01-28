print("Programa que convierte pies a yardas, pulgadas y metros")

pies= float(input("Escribe los pies: "))
yar_pi= 3
pul_pi= .08333
me_pi= .0254

yardas= pies*yar_pi
pulgadas=pies*pul_pi
metros=pies*me_pi

print("{0:.3f} yardas,{1:.3f} pulgadas,{2:.3f} metros.".format(yardas, pulgadas, metros))