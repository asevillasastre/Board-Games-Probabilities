cartas=[1,1,1,1,1,1,1,1,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,10,10,10,10,11,11,11,11,12,12,12,12,12,12,12,12]
import random
import time
from math import factorial

cartas=[1,1,1,1,2,2,2,2,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,10,10,10,10,11,11,11,11,12,12,12,12,3,3,3,3]


def quedan(mano):
    i=0
    deleted=0
    while deleted<4:
        if cartas[i]==mano[0]:
            cartas.pop(i)
            mano.pop(0)
            deleted+=1
        i+=1
        if i==len(cartas):
            i=0
    return cartas

def restomanos(mano,ite):
    t0=time.clock()
    result=[]
    while ite>0:
        new=[]
        cartas=[1,1,1,1,1,1,1,1,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,10,10,10,10,11,11,11,11,12,12,12,12,12,12,12,12]
        for j in range(4):
            aleatorio=random.randint(0,len(cartas)-1)
            new.append(cartas[aleatorio])
            cartas.pop(aleatorio)
        ite-=1
        print(ite)
        result.append(new)
    print(time.clock()-t0)
    return result

#restomanos([1,1,3,4],2*(factorial(36)//factorial(32)))

def medan(mano,manodescartada):
    t0=time.clock()
    cartas=[1,1,1,1,1,1,1,1,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,10,10,10,10,11,11,11,11,12,12,12,12,12,12,12,12]
    cartas=quedan(mano)
    if len(manodescartada)==0:
        return combinaciones4(cartas)
    if len(manodescartada)==1:
        return combinaciones3(cartas)
    if len(manodescartada)==2:
        return combinaciones2(cartas)
    if len(manodescartada)==3:
        return combinaciones1(cartas)
    if len(manodescartada)==0:
        return [mano]
    print(time.clock()-t0)

def combinaciones1(lst):
    result=[]
    for i in range(len(lst)):
        result.append([lst[i]])
    return result

def combinaciones2(lst):
    result=[]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            result.append([lst[i],lst[j]])
    return result

def combinaciones3(lst):
    result=[]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            for k in range(j+1,len(lst)):
                result.append([lst[i],lst[j],lst[k]])
    return result

def combinaciones4(lst):
    result=[]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            for k in range(j+1,len(lst)):
                for l in range(k+1,len(lst)):
                    result.append([lst[i],lst[j],lst[k],lst[l]])
    return result

#!!!!!!!!!!!!!!
#posibles=combinaciones4(cartas)
#!!!!!!!!!!!!!!

def matriculas(lst):
    result=[]
    for i in range(len(lst)):
        for j in range(len(lst)):
            for k in range(len(lst)):
                for l in range(len(lst)):
                    result.append([lst[i],lst[j],lst[k],lst[l]])
    return result

#ahora hay 40**4 combinaciones
posibles = matriculas(cartas)

def rotaciones(pieza):
    result=[]
    for i in range(len(pieza)):
        pie=[]
        j=0
        while j<len(pieza):
            pie.append(pieza[(i+j)%len(pieza)])
            j+=1
        result.append(pie)
    return result

def descarte(mano, manodescartada):
    a=medan(mano, manodescartada)
    for i in a:
        for j in manodescartada:
            i.insert(0,j)
    for k in a:
        print(k)
        k = sorted(k)
        print(k)
    return a

def sumajuego(mano):
    suma=0
    for carta in mano:
        if carta==3 or carta==11 or carta==12:
            suma+=10
        else:
            suma+=carta
    return suma

def juego(mano):
    if sumajuego(mano)==31:
        if mano==[7,7,7,10]:
            return 0
        return 1
    if sumajuego(mano)==32:
        return 2
    if sumajuego(mano)==40:
        return 3
    if sumajuego(mano)==37:
        return 4
    if sumajuego(mano)==36:
        return 5
    if sumajuego(mano)==35:
        return 6
    if sumajuego(mano)==34:
        return 7
    if sumajuego(mano)==33:
        return 8
    #########
    return 9
    #########

def array(lista,k):
    eureka=False
    i=0
    while i<len(lista)-1 and not eureka:
        j=0
        counter=0
        while j<len(lista):
            if lista[j]==lista[i]:
                counter+=1
            j+=1
        if counter==k:
            eureka=True
        i+=1
    if eureka==True:
        return lista[i-1]
    return False 


def pares(mano):
    #####################
    if mano in rotaciones([12,12,12,12]):
        return 0
    if array(mano,3)==12:
        return 36
    if array(mano,2)==12:
        return 44
    """
    if mano in rotaciones([12,12,12,12]):
        return 0
    if mano in rotaciones([12,12,11,11]):
        return 1
    if mano in rotaciones([12,12,10,10]):
        return 2
    if mano in rotaciones([12,12,7,7]):
        return 3
    if mano in rotaciones([12,12,6,6]):
        return 4
    if mano in rotaciones([12,12,5,5]):
        return 5
    if mano in rotaciones([12,12,4,4]):
        return 6
    if mano in rotaciones([12,12,1,1]):
        return 7
    if mano in rotaciones([11,11,11,11]):
        return 8
    if mano in rotaciones([11,11,10,10]):
        return 9
    if mano in rotaciones([11,11,7,7]):
        return 10
    if mano in rotaciones([11,11,6,6]):
        return 11
    if mano in rotaciones([11,11,5,5]):
        return 12
    if mano in rotaciones([11,11,4,4]):
        return 13
    if mano in rotaciones([11,11,1,1]):
        return 14
    if mano in rotaciones([10,10,10,10]):
        return 15
    if mano in rotaciones([10,10,7,7]):
        return 16
    if mano in rotaciones([10,10,6,6]):
        return 17
    if mano in rotaciones([10,10,5,5]):
        return 18
    if mano in rotaciones([10,10,4,4]):
        return 19
    if mano in rotaciones([10,10,1,1]):
        return 20
    if mano in rotaciones([7,7,7,7]):
        return 21
    if mano in rotaciones([7,7,6,6]):
        return 22
    if mano in rotaciones([7,7,5,5]):
        return 23
    if mano in rotaciones([7,7,4,4]):
        return 24
    if mano in rotaciones([7,7,1,1]):
        return 25
    if mano in rotaciones([6,6,6,6]):
        return 26
    if mano in rotaciones([6,6,5,5]):
        return 27
    if mano in rotaciones([6,6,4,4]):
        return 28
    if mano in rotaciones([6,6,1,1]):
        return 29
    if mano in rotaciones([5,5,5,5]):
        return 30
    if mano in rotaciones([5,5,4,4]):
        return 31
    if mano in rotaciones([5,5,1,1]):
        return 32
    if mano in rotaciones([4,4,4,4]):
        return 33
    if mano in rotaciones([4,4,1,1]):
        return 34
    if mano in rotaciones([1,1,1,1]):
        return 35
    ######################
    if array(mano,3)==11:
        return 37
    if array(mano,3)==10:
        return 38
    if array(mano,3)==7:
        return 39
    if array(mano,3)==6:
        return 40
    if array(mano,3)==5:
        return 41
    if array(mano,3)==4:
        return 42
    if array(mano,3)==1:
        return 43
    ######################
    if array(mano,2)==11:
        return 45
    if array(mano,2)==10:
        return 46
    if array(mano,2)==7:
        return 47
    if array(mano,2)==6:
        return 48
    if array(mano,2)==5:
        return 49
    if array(mano,2)==4:
        return 50
    if array(mano,2)==1:
        return 51
    ###########
    return 52
    ###########
    """
    if mano == list(set(mano)):
        return 55
    else:
        return 1

def tenerpares():
    #51710, 0.5658168289747237, '%'
    #con las matriculas es 0.9829 %
    result=0
    for i in posibles:
        if pares(i)<=51:
            result+=1
    return result, result/len(posibles), "%"

def tenerjuego():
    #24444, 0.2674690885217201, '%'
    #con las matriculas es 0.2768 %
    result=0
    for i in posibles:
        if juego(i)<=8:
            result+=1
    return result, result/len(posibles), "%"

def tener31():
    #8384, 0.09173870226501805, '%'
    #con las matriculas es 0.0912
    result=0
    for i in posibles:
        if juego(i)<=1:
            result+=1
    return result, result/len(posibles), "%"

def tenerreal():
    #48, 0.0005252215778531568, '%'
    #con las matriculas es 
    result=0
    for i in posibles:
        if juego(i)==0:
            result+=1
    return result, result/len(posibles), "%"

def tener4reyes():
    #70, 0.000765948134369187, '%'
    #con las matriculas es  0.0016
    result=0
    for i in posibles:
        if pares(i)==0:
            result+=1
    return result, result/len(posibles), "%"

def tener3reyes():
    #1862, 0.020374220374220375, '%'
    #con las matriculas es 0.0272
    result=0
    for i in posibles:
        if pares(i)==0 or pares(i)==36:
            result+=1
    return result, result/len(posibles), "%"

def tener2reyes():
    #13958, 0.1527300579932159, '%'
    #con las matriculas es 0.1688
    result=0
    for i in posibles:
        if pares(i)==0 or pares(i)==36 or pares(i)==44:
            result+=1
    return result, result/len(posibles), "%"

def tener1rey():
    #32485, 0.3554546449283291, '%'
    #con las matriculas es 0.5904
    result=0
    for i in posibles:
        if 12 in i:
            result+=1
    return result, result/len(posibles), "%"

def grande(mano):
    result=0
    i=0
    while i<len(mano):
        if mano[i]==3:
            mano[i]=12
        i+=1
    for carta in mano:
        if carta==12:
            result+=10**7
        if carta==11:
            result+=10**6
        if carta==10:
            result+=10**5
        if carta==7:
            result+=10**4
        if carta==6:
            result+=10**3
        if carta==5:
            result+=10**2
        if carta==4:
            result+=10**1
        if carta==1:
            result+=10**0
    return result

def ganargrande(mano):
    result=0
    a=grande(mano)
    todas=0
    for i in combinaciones4(quedan(mano)):
        ###LA MANO###
        if grande(i)<a:
            result+=1
        todas+=1
    return (result/todas)*100

def ganarpares(mano):
    result=0
    a=pares(mano)
    conpares=0
    for i in combinaciones4(quedan(mano)):
        ###LA MANO###
        if pares(i)>=a and pares(i)<52:
            result+=1
        if pares(i)<52:
            conpares+=1
    return (result/conpares)*100





