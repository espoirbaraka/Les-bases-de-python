#RENVOI LES CODES HTML D'UNE PAGE WEB
import requests
resp = requests.get('https://www.isig.ac.cd/')
html=resp.text
print(html[1:100000])