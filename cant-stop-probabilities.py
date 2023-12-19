"""
CANT STOP
"""

"""generamos todas las jugadas posibles, algunas repetidas por supuesto"""
posibles = []

for d1 in range(1,7):
    for d2 in range(1,7):
        for d3 in range(1,7):
            for d4 in range(1,7):
                posibles.append([d1,d2,d3,d4])

def jugadas(resultado):
    """ resultado = [d1,..,d4]
    jugadas posibles a hacer con un resultado"""
    result = []
    for i1 in range(4):
        for i2 in range(4):
            if i1 != i2:
                result.append(sorted([resultado[i1]+resultado[i2],
                               resultado[[list(set(range(4))-{i1,i2})][0][0]] + \
                                   resultado[[list(set(range(4))-{i1,i2})][0][1]]
                                ]))
    setresult = []
    for i in result:
        if i not in setresult:
            setresult.append(i)
    return setresult
   
def seguir(cogidos, resultado):
    """sigues jugando teniendo en cuenta los peones cogidos
    tras la tirada resultado?"""
    for i in jugadas(resultado):
        for k in i:
            for j in cogidos:
                if k == j:
                    return True
    return False     

def P_s(cogidos):
    """cogidos = los numeros en los que pones tus peones ese turno = [3,6,7] p.ej."""
    """calcula la probabilidad de seguir"""
    buenas = 0
    for p in posibles:
        if seguir(cogidos, p):
            buenas+=1
    return round(buenas/len(posibles),4)

def P_s_n(cogidos, seguidos):
    """calcula la probabilidad de seguir despues de n tiradas"""
    return round((P_s(cogidos))**seguidos, 4)

"""de alguna manera vanos a ver cuánto toca cada número y cuánto son de buenos
   teniendo en cuenta la cantidad de veces que hay que sacarlo para obtener 1 pto de victoria"""
for i in range(2,13):
    print("i: ", i)
    print("P(i):", P_s([i]))
    n = 13 - abs(7-i)*2       #está chulo porque 13 y 2 quizá sean los que hacen m más homogéneo en i
    m = round(P_s([i])/n, 4)
    print("P(i)/n: ",m)
    print("----------------")

#podemos intentar cambiar 13 y 2 a ver si estabilizan más m con otros números
#sin embargo lo mejor sería otro estimador que no sea m para "cuánto compensa ir a un número"