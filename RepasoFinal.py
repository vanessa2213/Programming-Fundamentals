#Ejercicios de practica 1
def EliminaDuplicados(lista):
    re=[]
    for i in lista:
        if i in lista and i not in re:
            re.append(i)
    return re

def ConDuplicados(lista):
    lis=[]
    for i in lista:
        if i in lista and i not in lis:
            lis.append(i)
        elif i in lista and i in lis:
            return True
    return False

def Ordenada(lista):
    num=-1
    valor=0
    for i in lista:
        if i>num:
            num=i
            valor=1
        else:
            valor=2
            break
    if valor==1:
        return True
    else:
        return False

def Invierte(lista):
    num=len(lista)-1
    lis=[]
    for i in lista:
        lis.append(lista[num])
        num-=1
    return lis

def PalabrasConMasDe(string,num):
    cont=0
    string=string.split(" ")
    for i in string:
        if len(i)==num:
            cont+=1
    return cont

def Espaciado(string):
    string=string.replace(" ","")
	lis=""
	for i in string:
		lis=lis+i
		lis=lis+ " "
	return newlista

#Ejercicios de practica 2
def CombinaListas(lista1,lista2):
    
