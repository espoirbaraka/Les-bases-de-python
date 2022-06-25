# La fonction continue() permet de sauter seulement Burundi et de continuer
pays = ['RDC','Rwanda','Burundi','Tanzanie','Ouganda','Kenya']
for x in pays:
    if(x == 'Burundi'):
        continue
    print(x)

# La fonction break() permet de s'arreter lorsque la boucle trouve Burundi
pays = ['RDC','Rwanda','Burundi','Tanzanie','Ouganda','Kenya']
for x in pays:
    if(x == 'Burundi'):
        break
    print(x)