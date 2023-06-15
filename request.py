import requests
from bs4 import BeautifulSoup

url = 'https://fr.wikipedia.org/wiki/Liste_des_pays_par_population'

response = requests.get(url)

if response.ok:
    country_names = []
    soup = BeautifulSoup(response.text, 'lxml')
    tds = soup.findAll('td')
    for td in tds:
        span = td.find('span')
        if span:
            country_name = span['data-sort-value']
            country_names.append(country_name)

    print(country_names)