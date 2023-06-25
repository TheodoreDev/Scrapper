import csv
import time
import requests
from bs4 import BeautifulSoup


while True:
    dataFile = "data/data.csv"
    header = ["Country", "Inhabitants", "IDHI"]

    Country = []
    Inhabitants = []
    IDHI = []
    ii = 0

    url = 'https://fr.wikipedia.org/wiki/Liste_des_pays_par_population'

    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        tds = soup.findAll(class_='datasortkey')
        trs = soup.findAll('tr')

        for a in tds:
            try:
                name = a.find('a', class_ = not('flagicon')).text.strip()
            except Exception as e:
                name = 'Îles Turques-et-Caïques'
            Country.append(name)
        for td in trs:
            try:
                if ii > 1:
                    number = td.find('td', attrs={'align' : 'right'}).text.strip()
                    Inhabitants.append(number)
                ii = ii + 1
            except Exception as e:
                number = None

    number_country = len(Country)

    for i in range(number_country):
        url2 = f'https://fr.wikipedia.org/wiki/{Country[i]}'

        response2 = requests.get(url2)
        ahref = []

        if response2.ok:
            soup2 = BeautifulSoup(response2.text, 'html.parser')
            a = soup2.findAll('a', attrs={'title': 'Liste des pays par IDH ajusté selon les inégalités'})
            for all in a:
                ahref.append(all)
            try:
                idhi_children = ahref[1]
                idhi1 = idhi_children.find_parent('td')
                idhi = idhi1.text.strip()
                idhi_final = idhi[0:5]
            except Exception as e:
                idhi_final = None
            IDHI.append(idhi_final)


    with open(dataFile, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerow(header)
        for i in range(number_country):
            writer.writerow([f"{Country[i]}", f"{Inhabitants[i]}", f"{IDHI[i]}"])

    print("update")
    time.sleep(2)