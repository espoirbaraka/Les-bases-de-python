#CETTE FONCTION NOUS PERMET DE SAISIR 2 NOMBRE ET ELLE DONNE LA SOMME DE CES 2 NOMBRES
#         NB :La fonction eval() permet d'executer une chaine de caractères en tant qu'instruction
def somme():
    x=eval(input("Saisi un nombre \n"))
    y=eval(input("Saisissez un autre \n"))
    print("La somme de {} et {} est {}".format(x,y,x+y))
somme()