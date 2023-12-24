# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 23:01:50 2022

@author: Toni
"""


import random

def num_repetidos(num_sobres, cromos_por_sobre, cromos_totales):
    totales = []
    for i in range(num_sobres):
        sobre = []
        while len(sobre) < cromos_por_sobre:
            cromo = random.randint(1, cromos_totales)
            if cromo not in sobre:
                sobre.append(cromo)
        #print(sobre)
        for cromo in sobre:
            totales.append(cromo)
    repetidos = len(totales) - len(list(set(totales)))
    return repetidos, round(100*repetidos/(num_sobres*cromos_por_sobre), 2), \
        cromos_totales - len(list(set(totales)))

cromos_tot = 32*20 + 30

#num_sob = 43
#print(num_repetidos(num_sob, 5, cromos_tot))

"""
for i in range(1_000):
    a = num_repetidos(num_sob, 5, cromos_tot)[0]
    if a < 15:
        print(a)
"""

#fer_sob = 200
#print(num_repetidos(fer_sob, 5, cromos_tot))

#lore_sob = 25
#print(num_repetidos(lore_sob, 5, cromos_tot))




