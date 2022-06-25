#UN DICTIONNAIRE REGROUPE PLUSIEURS ELEMENTS. CHAQUE ELEMENT AVEC UNE CLE ET 1 OU PLUSIEURS VALEURS
# Logique Clé-valeur

FrancaisAnglais = {'papa':'dad', 'moi':'me', 'toi':'you'}
Points = {'Biologie':[10,10,14,11], 'Francais':[12,25,12]}

#retourne le dictionnaire FrancaisAnglais
print(FrancaisAnglais.items())

#Retourne les clé
print(FrancaisAnglais.keys())

#Retourne les valeurs
print(FrancaisAnglais.values())

#La taille du dictionnaire
print(len(Points))

#Affiche aussi le dictionnaire
print(str(Points))