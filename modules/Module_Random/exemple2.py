#Ce script permet de jouer au Jeux Mundele 4 fois
from random import randint
print("Essayer votre chance")
print()
for z in range(4):
    x=eval(input("Saisi un nombre \n"))
    w=randint(1,4)
    if(x==w):
        print("Felicitation!!! Vous avez gagné")
    else:
        print("Desole {} n'est pas admis".format(x))