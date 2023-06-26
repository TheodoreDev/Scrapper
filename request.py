import csv
import time
import requests
from bs4 import BeautifulSoup

url2 = f'https://fr.wikipedia.org/wiki/Birmanie'

response2 = requests.get(url2)
ahref = []

if response2.ok:
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    sups = soup2.find('sup', attrs={'id' : 'cite_ref-hdr2021-22_7-1'})
    idhi1 = sups.find_parent('td')
    idhi = idhi1.text.strip()
    idhi_final = idhi[0:5]
    print(idhi_final)
