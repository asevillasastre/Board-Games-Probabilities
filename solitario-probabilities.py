# -*- coding: utf-8 -*-
"""
CALCULO DE LA PROBABILIDAD DE GANAR AL "SOLITARIO CAPICÚA"

Created on Sat Aug 13 15:50:38 2022 on San Vicente de la Barquera

@author: Toni
"""
import random
import time
import winsound
import math

#creamos una lista de cartas posibles
cartas = []
for number in [1,2,3,4,5,6,7,10,11,12]:
    for palo in ["O", "C", "E", "B"]:
        cartas.append({number, palo})
        
#print(cartas)
#print(type(cartas[1]))
#len(cartas)
        
#jugamos una partida de "s-c"
def p():
    cartas = [{1, 'O'}, {1, 'C'}, {1, 'E'}, {1, 'B'}, {2, 'O'}, {2, 'C'}, 
              {2, 'E'}, {2, 'B'}, {3, 'O'}, {'C', 3}, {3, 'E'}, {3, 'B'}, 
              {4, 'O'}, {'C', 4}, {4, 'E'}, {'B', 4}, {5, 'O'}, {'C', 5}, 
              {5, 'E'}, {'B', 5}, {6, 'O'}, {'C', 6}, {6, 'E'}, {'B', 6}, 
              {'O', 7}, {'C', 7}, {'E', 7}, {'B', 7}, {10, 'O'}, {10, 'C'}, 
              {10, 'E'}, {10, 'B'}, {11, 'O'}, {'C', 11}, {11, 'E'}, {11, 'B'},
              {12, 'O'}, {'C', 12}, {12, 'E'}, {'B', 12}]
    puestas = []
    #mientras queden cartas en el mazo
    while len(cartas) > 0:
        #print("\n", puestas,"\n")
        #escogemos una carta al azar del mazo
        a = random.randint(0,len(cartas)-1)
        #la ponemos a continuacion
        ###print("\n", cartas[a])
        puestas.append(cartas[a])
        #la quitamos del mazo
        cartas.pop(a)
        #miramos si las montamos DE IZQUIERDA A DERECHA
        while True:
            #print("---")
            i = 0
            j = 0
            while i < len(puestas) - 2:
                #print(i, puestas[i], puestas[i+2])
                if len(puestas[i]&puestas[i+2]) == 1:
                    j = i
                    break
                i+=1
            if i == len(puestas) - 2 or len(puestas) <= 2:
                break
            else:
                #print(puestas,"\n")
                puestas[j] = puestas[j+1]
                puestas.pop(j+1)
                #print(j)
                #print("\n",puestas)
    if len(puestas) == 2:
        #print("\n", True)
        return 2
    else:
        #print("\n",len(puestas))
        #print(puestas)
        return len(puestas)

def prueba_(intentos):
    t0 = time.clock()
    gano = 0
    for i in range(intentos):
        if p() == 2:
            gano += 1
    print(str(intentos) + " intentos\n" +
          str(round(gano/intentos, 3)*100)+ " % de victorias\n" + 
          "en " + str(round(time.clock()-t0, 3)) + " segundos")
    winsound.Beep(1200, 1200)

#la media al final es de 15.111 cartas o así

#de momento puedo hacer 200000 partidas al minuto              

def prueba(minutos):
    intentos = int(minutos*200000)
    t0 = time.clock()
    gano = 0
    for i in range(intentos):
        if p() == 2:
            gano += 1
    print(str(intentos) + " intentos\n" +
          str(round(gano/intentos, 3)*100)+ " % de victorias\n" + 
          "en " + str(round(time.clock()-t0, 3)) + " segundos")
    winsound.Beep(1200, 1200)
        
"""prueba(45)
9000000 intentos
0.5 % de victorias
en 2612.775 segundos"""