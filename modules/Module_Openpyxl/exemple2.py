from  openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.chart.label import DataLabelList

wb = Workbook()
feuille1 = wb.active
lignes = [
    ["Nom boisson", "Nombre bouteilles"],
    ["Primus", 221],
    ["Jus", 18],
    ["Castle", 92],
    ["Mutzig", 165],
    ["Virunga", 71],
    ["Champagne", 9],
    ["J.walker", 19],
    ["Tusker", 21],
    ["Sucrés", 283],
    ["Skol", 79]]

for i in lignes:
    feuille1.append(i)
chart = BarChart()
values = Reference(worksheet=feuille1, min_row=1, max_row=11, min_col=2,max_col=2)
chart.dataLabels = DataLabelList()
chart.dataLabels.showVal = True   #Montre les valeurs
chart.add_data(values, titles_from_data=True)

marques = Reference(feuille1, min_col=1, min_row=2, max_row=11) #Preciser les cellules concernées
chart.set_categories(marques)   #ajouter les étiquettes sur le chart
feuille1.add_chart(chart, 'E2')

wb.save("Boisson.xlsx")

