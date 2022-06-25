from random import *
print("Essayer votre chance")
print()
x=eval(input("Saisi un nombre \n"))
w=randint(1,4)
if(x==w):
    print("Felicitation!!! Vous avez gagné")
else:
    print("Desole {} n'est pas admis".format(x))