import csv
import time
import requests
from bs4 import BeautifulSoup

url2 = f'https://fr.wikipedia.org/wiki/Chine'

response2 = requests.get(url2)
ahref = []

if response2.ok:
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    a = soup2.findAll('a', attrs={'title' : 'Liste des pays par IDH ajusté selon les inégalités'})
    for all in a:
        ahref.append(all)
    idhi_children = ahref[1]
    idhi1 = idhi_children.find_parent('td')
    idhi = idhi1.text.strip()
    print(idhi[0:5])