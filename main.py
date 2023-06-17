import csv
import time
import requests
from bs4 import BeautifulSoup

url = 'https://fr.wikipedia.org/wiki/Liste_des_pays_par_population'

response = requests.get(url)

if response.ok:
    while True:
        dataFile = "data/data.csv"
        header = ["Country", "Inhabitants"]

        Country = []
        Inhabitants = []
        ii = 0
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



        with open(dataFile, "w", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow(header)
            for i in range(number_country):
                writer.writerow([f"{Country[i]}", f"{Inhabitants[i]}"])

        print("update")
        time.sleep(2)