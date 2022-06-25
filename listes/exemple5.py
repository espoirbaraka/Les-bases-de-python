#Ce script permet de saisir continuellement un pays dans une liste si l'utilisateur saisi 'Y'
pays = list()
reponse = 'y'
while reponse=='y' or reponse=='Y':
    x=input("Saisissez un pays \n")
    pays.append(x)
    reponse=input("Voulez-vous continuer?")
print(pays)