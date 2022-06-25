pays = ['RDC','Rwanda','Burundi','Tanzanie','Ouganda','Kenya']
x = input("Saisi un pays \n")
if x in pays:
    print("{} est sur la liste".format(x))
else:
    print("{} n'est pas sur la liste".format(x))