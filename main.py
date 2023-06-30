import csv
import time
import requests
from bs4 import BeautifulSoup


while True:
    dataFile = "data/data.csv"
    header = ["Country", "Inhabitants", "IDHI", "PIB /hab"]

    Country = []
    Inhabitants = []
    IDHI = []
    PIB = []
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
        if Country[i] == "Équateur":
            url2 = 'https://fr.wikipedia.org/wiki/%C3%89quateur_(pays)'
        elif Country[i] == "Irlande":
            url2 = 'https://fr.wikipedia.org/wiki/Irlande_(pays)'
        else:
            url2 = f'https://fr.wikipedia.org/wiki/{Country[i]}'

        response2 = requests.get(url2)
        ahref = []
        ahref2 = []
        tr_index = []
        tr_index2 = []
        idhi_final = None
        pib_final = None

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
                try:
                    soup2 = BeautifulSoup(response2.text, 'html.parser')
                    caps = soup2.findAll('caption', attrs={'style': 'background-color:#e3e3e3;'})
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
                except Exception as e:
                    idhi_final = None
            IDHI.append(idhi_final)

            try:
                soup3 = BeautifulSoup(response2.text, 'html.parser')
                caps2 = soup3.findAll('caption', attrs={'style': 'background-color:#e3e3e3;'})
                for cap in caps2:
                    if cap.text == "Économie":
                        table_children2 = cap
                        table2 = table_children2.find_parent('table')
                        tbody2 = table2.find('tbody')
                        trs2 = tbody2.findAll('tr')
                        for tr in trs2:
                            tr_index2.append(tr)
                        tr_good2 = tr_index2[2]
                        th2 = tr_good2.find('th')
                        if th2.find('a').text == "PIB nominal":
                            td2 = tr_good2.find('td')
                            pib = td2.text.strip().replace("dollars", "$").split('$')
                            pib_final = pib[0].replace("de", "").strip().replace(",", ".")
                        else:
                            pib_final = None
            except Exception as e:
                pib_final = None
            PIB.append(pib_final)
            print(Country[i] + " : " + str(pib_final))


    with open(dataFile, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerow(header)
        for i in range(number_country):
            writer.writerow([f"{Country[i]}", f"{Inhabitants[i]}", f"{IDHI[i]}", f"{PIB[i]}"])

    print("update")