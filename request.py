import csv
import time
import requests
from bs4 import BeautifulSoup

url2 = f'https://fr.wikipedia.org/wiki/Birmanie'

response2 = requests.get(url2)
tr_index = []
table_children = None

if response2.ok:
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    caps = soup2.findAll('caption', attrs={'style' : 'background-color:#e3e3e3;'})
    for cap in caps:
        if cap.text == "Développement":
            table_children = cap
            table = table_children.find_parent('table')
            tbody = table.find('tbody')
            trs = tbody.findAll('tr')
            for tr in trs:
                tr_index.append(tr)
            tr_good = tr_index[1]
            th = tr_good.find('th')
            if th.find('a').text == "IDHI":
                td = tr_good.find('td')
                idhi = td.text.strip()
                idhi_final = idhi[0:5]
            else:
                idhi_final = None

    print(str(idhi_final))
