#ORDONNE LES NOMS
from random import *
noms = ['Baraka','Bigega','Espoir','Siwa','Gabin']
newlist = []
for y in range(5):
    x = choice(noms)
    newlist.append(x)
    noms.remove(x)
    print("{} . {} ".format(y,x))
print("Ce triage a été effectué sur cette liste {} :".format(newlist))
