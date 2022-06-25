# Fonction type() : nous retourne le type des données
pays = ['RDC','Rwanda','Burundi','Tanzanie','Ouganda','Kenya']
print(type(pays))

#Affiche un element de la position 1
print(pays[1])

# Voici un script qui permet de saisir 10 pays et les afficher
# Fonction range permet d'iterer
pays=list()
for x in range(10):
    y = input("Saisi un pays")
    pays.append(y)
print(pays)


