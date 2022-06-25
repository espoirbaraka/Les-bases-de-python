#CHOISE CHOISI ALEATOIREMENT UN STRING PARMIS PLUSIEURS
from random import *
noms = ['Baraka','Bigega','Espoir','Siwa','Gabin']
for y in range(5):
    x = choice(noms)
    noms.remove(x)
    print("{} . {} ".format(y,x))
