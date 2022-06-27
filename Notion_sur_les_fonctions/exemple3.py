#FACTURE
stock = {'Sucre':500, 'Pain':950, 'Huile':1500, 'Savon':200, 'Riz':720}
def lestock(x):
    for i in stock:
        print(str(i).rjust(10), ' ',str(x[i]).rjust(10)+'Fr')

def sommeproduit(x):
    prix = []
    for j in stock:
        prix.append(x[j])
    print('LE PRIX TOTAL A PAYER EST : '.rjust(10), sum(prix))

def tracer(v,w):
    print(v*w)

tracer('*',40)
print("\t\t BOUTIQUE St PIERRE")
tracer('*',40)
print('PRODUITS'.rjust(10),'PRIX'.rjust(17))
tracer('.',40)
lestock(stock)
tracer('.',40)
sommeproduit(stock)
tracer('.',40)