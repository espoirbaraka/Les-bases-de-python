from tkinter import *
fen = Tk()
fen.title("Exercice de python")
fen.geometry('500x400')
fen.config(bg='#54cbf4')
Etiquette = Label(text ="FICHE DE L'ETUDIANT",bg='#54cbf4',fg='black',font='bold')
Etiquette.grid(column=12, row=1)
Nom = Label(text ="Nom: BARAKA",bg='#54cbf4',fg='black',font='bold')
Nom.grid(column=6, row=3)
Postnom = Label(text ="Postnom: BARAKA",bg='#54cbf4',fg='black',font='bold')
Postnom.grid(column=6, row=4)
Prenom = Label(text ="Prenom: BARAKA",bg='#54cbf4',fg='black',font='bold')
Prenom.grid(column=6, row=5)
fen.mainloop()