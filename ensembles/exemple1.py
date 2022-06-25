prisonnier = {"SIWA","STEVEN","BAMONGOYO","ALBERT"}
etudiant = {"ESPOIR","BARAKA","SIWA","STEVEN"}
motard = {"AKETI","SIWA","STEVEN","FEZA"}
birere = {"ESPOIR","JUSTINE","BAMONGOYO","FEZA"}

#Les motards de birere
motardbirere = motard.intersection(birere)
print(motardbirere)

#Les motard qui n'ont jamais été en prison
motardjamaisprison = motard.difference(prisonnier)
print(motardjamaisprison)

#Ajoute DARCIN sur la liste des prisonniers
prisonnier.add("DARCIN")
print(prisonnier)
