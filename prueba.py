import random
def revuelvePalabra(s):
	re=""
	i=0
	while i<len(s):
		pos=random.randint(0,(len(s)-1))
		re+=s[pos]
		i+=1
		s-=s[pos]
	return re


s=input("Escribe: ")
print(revuelvePalabra(s))
