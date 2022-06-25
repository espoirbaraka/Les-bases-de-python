#UN ENSEMBLE EST UN GROUPEMENT NON-ORDONNE D'ELEMENT UNIQUE

prisonnier = {"SIWA","STEVEN","BAMONGOYO","ALBERT"}
etudiant = {"ESPOIR","BARAKA","SIWA","STEVEN"}
motard = {"AKETI","SIWA","STEVEN","FEZA"}
birere = {"ESPOIR","JUSTINE","BAMONGOYO","FEZA","AKETI","SIWA","STEVEN"}

#Les motards de birere
motardbirere = motard.intersection(birere)
print(motardbirere)

#Les motard qui n'ont jamais été en prison
motardjamaisprison = motard.difference(prisonnier)
print(motardjamaisprison)

#Ajoute DARCIN sur la liste des prisonniers
prisonnier.add("DARCIN")
print(prisonnier)

#Motard UNION etudiant
motardetetudiant = motard.union(etudiant)
print(motardetetudiant)

#Si tout les motard vivent à birere
tout_les_motard_sont_a_birere = motard.issubset(birere)
print(tout_les_motard_sont_a_birere)
