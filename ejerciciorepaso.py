#ejercicio de repaso 1
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
        lis+=i
        lis+= " "
    return newlista

#ejercio repaso 2
def combina_listas1(lista1,lista2):
    n=[]
    pos=0
    if len(lista1)>len(lista2):
        while len(lista2)>pos:
            n.append(lista1[pos])
            n.append(lista2[pos])
            pos+=1
        for i in range(pos,len(lista1)):
            n.append(lista1[pos])
    elif len(lista1)<len(lista2):
        while len(lista1)>pos:
            n.append(lista2[pos])
            n.append(lista1[pos])
            pos+=1
        for i in range(pos,len(lista1)):
            n.append(lista2[pos])
    else:
        for i in range(0,len(lista1)):
            n.append(lista1[i])
            n.append(lista2[i])
    return n
    
def combina_lista(lista1,lista2):
    x = len(lista1)
    y = len(lista2)
    cont1 = 0
    z = max(x,y)-1
    nl = []
    while cont1 < z:
        nl.append(lista1[cont1])
        nl.append(lista2[cont1])
        cont1 += 1
        for i in range (cont1,y):
            nl.append(lista2[i])
    return nl
def combina_lista2(lista1,lista2):
    x = len(lista1)
    y = len(lista2)
    cont = 0
    z = max(x,y)-1
    nl = []
    while cont < z:
        nl.append(lista1[cont])
        nl.append(lista2[cont])
        cont += 1
        for x in range (cont, y):
            nl.append(lista2[x])
    return nl

print(combina_lista2([1,2], [3,4,5]))