#Voici un module qui permet d'afficher le factoriel d'un nombre saisi
#Factoriel de 5 = 5*4*3*2*1
from math import *
v=eval(input("Saisi un nombre \n"))
print("Le factoriel de {} est {}".format(v,factorial(v)))
