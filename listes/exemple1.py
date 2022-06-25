#Ce programme demande de saisir un pays.
# si le pays est dans la liste, il repond 'Pays est dans la liste', si non 'Pays n'est pas dans la liste'

pays = ['RDC','Rwanda','Burundi','Tanzanie','Ouganda','Kenya']
x = input("Saisi un pays \n")
if x in pays:
    print("{} est sur la liste".format(x))
else:
    print("{} n'est pas sur la liste".format(x))