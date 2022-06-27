#PREVISION DES MATCH DE LA COUPE DU MONDE
from random import *
groupe_A = ['Qatar','Equateur','Senegal','Pays-bas']
date_groupe_A = ['le 21/11/2022', 'le 22/11/2022', 'le 22/11/2022','le 23/11/2022', 'le 23/11/2022', 'le 24/11/2022']
groupe_B = ['Angleterre','Iran','Etats-unis','Pays des Galles']
date_groupe_B = ['le 22/11/2022', 'le 22/11/2022', 'le 23/11/2022','le 23/11/2022', 'le 24/11/2022', 'le 24/11/2022']
groupe_C = ['Argentine','Arabie saoudite','Mexique','Pologne']
date_groupe_C = ['le 22/11/2022', 'le 23/11/2022', 'le 23/11/2022','le 24/11/2022', 'le 24/11/2022', 'le 25/11/2022']
groupe_D = ['France','Australie','Danemark','Tunisie']
date_groupe_D = ['le 23/11/2022', 'le 23/11/2022', 'le 24/11/2022','le 24/11/2022', 'le 25/11/2022', 'le 25/11/2022']
groupe_E = ['Espagne','Costa-rica','Allemagne','Japon']
date_groupe_E = ['le 24/11/2022', 'le 24/11/2022', 'le 25/11/2022','le 25/11/2022', 'le 26/11/2022', 'le 26/11/2022']
groupe_F = ['Belgique','Canada','Maroc','Croatie']
date_groupe_F = ['le 24/11/2022', 'le 25/11/2022', 'le 25/11/2022','le 26/11/2022', 'le 26/11/2022', 'le 27/11/2022']
groupe_G = ['Bresil','Serbie','Suisse','Cameroun']
date_groupe_G = ['le 25/11/2022', 'le 25/11/2022', 'le 26/11/2022','le 26/11/2022', 'le 27/11/2022', 'le 27/11/2022']
groupe_H = ['Portugal','Ghana','Uruguay','Coree du sud']
date_groupe_H = ['le 25/11/2022', 'le 26/11/2022', 'le 26/11/2022','le 27/11/2022', 'le 27/11/2022', 'le 28/11/2022']

match_deja_planifie_A = []
date_deta_planifie_A = []
print("VOICI LE CALENDRIER DU PHASE DES GROUPE DE LA COUPE DU MONDE")
print("============================================================ \n")
print("GROUPE A")
for y in range(6):
    #Date
    date = choice(date_groupe_A)
    date_groupe_A.remove(date)
    equipe_A = choices(groupe_A, k=2)

    print("{} : {} vs {}".format(date, equipe_A[0], equipe_A[1]))

print("\n GROUPE B")
for y in range(6):
    #Date
    date = choice(date_groupe_B)
    date_groupe_B.remove(date)
    equipe_B = choices(groupe_B, k=2)

    print("{} : {} vs {}".format(date, equipe_B[0], equipe_B[1]))

print("\n GROUPE C")
for y in range(6):
    #Date
    date = choice(date_groupe_C)
    date_groupe_C.remove(date)
    equipe_C = choices(groupe_C, k=2)

    print("{} : {} vs {}".format(date, equipe_C[0], equipe_C[1]))

print("\n GROUPE D")
for y in range(6):
    #Date
    date = choice(date_groupe_D)
    date_groupe_D.remove(date)
    equipe_D = choices(groupe_D, k=2)

    print("{} : {} vs {}".format(date, equipe_D[0], equipe_D[1]))

print("\n GROUPE E")
for y in range(6):
    #Date
    date = choice(date_groupe_E)
    date_groupe_E.remove(date)
    equipe_E = choices(groupe_E, k=2)

    print("{} : {} vs {}".format(date, equipe_E[0], equipe_E[1]))

print("\n GROUPE F")
for y in range(6):
    #Date
    date = choice(date_groupe_F)
    date_groupe_F.remove(date)
    equipe_F = choices(groupe_F, k=2)

    print("{} : {} vs {}".format(date, equipe_F[0], equipe_F[1]))

print("\n GROUPE G")
for y in range(6):
    #Date
    date = choice(date_groupe_G)
    date_groupe_G.remove(date)
    equipe_G = choices(groupe_G, k=2)

    print("{} : {} vs {}".format(date, equipe_G[0], equipe_G[1]))

print("\n GROUPE H")
for y in range(6):
    #Date
    date = choice(date_groupe_H)
    date_groupe_H.remove(date)
    equipe_H = choices(groupe_H, k=2)

    print("{} : {} vs {}".format(date, equipe_H[0], equipe_H[1]))