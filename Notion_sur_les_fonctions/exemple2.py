#Cette fonction 4 lignes en utilisant une fonction à 2 arguments(symbole, taille)
def tracer(symbole, taille):
    for x in range(4):
        print(symbole * taille)
x=str(input("Saisi un symbole \n"))
y=eval(input("Saisi la taille \n"))
tracer(x,y)