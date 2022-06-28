from openpyxl import Workbook
wb = Workbook()
feuille1 = wb.active
feuille1["A1"]="NOMS"
feuille1["C1"]="COURS"
feuille1["B2"]="MATH"
feuille1["C2"]="FRANCAIS"
feuille1["D2"]="ANGLAIS"

x = (('HERI',20,30,48),('AWA',20,22,48),('EMMA',20,34,45),('KOKO',20,30,48),('MAMY',20,30,48),('ELIE',20,30,48))
for i in x:
    feuille1.append(i)
wb.save("Fichier.xlsx")