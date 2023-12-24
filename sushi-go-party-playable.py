import random
#import numpy as np

class P:
    
    def __init__(self, mano1, mano2, turnos):
        self.manoPC = mano1
        self.manoH = mano2
        self.playedPC = []
        self.playedH = []
        self.puntPC = 0
        self.puntH = 0
        self.turnos = turnos
        
    def __repr__(self):
        return "\nmanoPC: " + str(self.playedPC) + "\npuntPC: " + str(self.puntPC) + \
        "\nmanoH:  " + str(self.playedH) + "\npuntH:  " + str(self.puntH)
    def __print__(self):
        return "\nmanoPC: " + str(self.playedPC) + "\npuntPC: " + str(self.puntPC) + \
        "\nmanoH:  " + str(self.playedH) + "\npuntH:  " + str(self.puntH)
    def __int__(self):
        return "\nmanoPC: " + str(self.playedPC) + "\npuntPC: " + str(self.puntPC) + \
        "\nmanoH:  " + str(self.playedH) + "\npuntH:  " + str(self.puntH)
        
    def swapcards(self):
        self.manoPC, self.manoH = self.manoH, self.manoPC
        
    def playcardPC(self, cardPC):
        self.manoPC.remove(cardPC)
        self.playedPC.append(cardPC)
        
    def playcardH(self, cardH):
        self.manoH.remove(cardH)
        self.playedH.append(cardH)
        
    def classcounter(self):
        self.puntPC = counter(self.playedPC)
        self.puntH = counter(self.playedH)

def counter(mano):
    result = sum(mano)
    return result
        
def erandom(mano, IA_):
    ponders = list(range(len(mano)))
    for i in range(len(mano)):
        ponders[i] = IA_.net[mano[i]]
    return random.choices(mano, ponders)
    return mano[random.randint(0,len(mano)-1)]

def partidahumana(P1, IA_):
    P1
    while len(P1.playedPC) < P1.turnos:
        escogida = int(input("escoge una carta entre " + str(P1.manoH) + "\n"))
        P1.playcardH(escogida)
        #########################################
        P1.playcardPC(erandom(P1.manoPC, IA_))
        #########################################
        P1.swapcards()
    P1.classcounter()
    #print(P1)
    return P1

class IA:
    
    def __init__(self, kinds):
        self.kinds = kinds
        auxdict = {}
        for i in kinds:
            auxdict[i] = 1
        self.net = auxdict
    
    def __repr__(self):
        auxnet = {}
        for i in self.net.keys():
            num = float(self.net[i])
            auxnet[i] = round(num,3)
        return str(auxnet)
    
    def feedback(self, hand, win, cookies):
        a = cookies
        if not win:
            a = -cookies
        for card in hand:
            self.net[card] += a

#Peje = P([1,2,3],[2,3,4], 3)
#partidahumana(Peje)
#Gla1 = IA([1,2,3,4,5])
#Gla1.feedback([1,2,3],0,0.2)

def sethumano(kinds, tur, galletas):
    Gla1 = IA(kinds)
    continuar = "sí"
    marcador = [0,0]
    while continuar.lower() in ["sí", "si", "sep", "síç", "siç", "y"]:
        mano1, mano2 = [], []
        for i in range(tur):
            mano1.append(kinds[random.randint(0,len(kinds)-1)])
            mano2.append(kinds[random.randint(0,len(kinds)-1)])
        Pset = P(mano1, mano2, tur)
        partidahumana(Pset, Gla1)
        pcwin = int(Pset.puntPC >= Pset.puntH)
        Gla1.feedback(Pset.playedPC, pcwin, galletas)
        if pcwin:
            marcador[1]+=1
        else:
            marcador[0]+=1
        proppcwin = marcador[1]/sum(marcador)
        print(Gla1)
        print(marcador)
        print(proppcwin)
        continuar = input("\n¿CONTINUAR JUGANDO? ")

sethumano([1,2,3,4,5], 3, 0.2)






