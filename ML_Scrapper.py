from create_database import create_database
from web_retriever import get_url
import sqlite3
import re

print ("\n ----------------------------")
print ("| Welcome to Mati's Scrapper |")
print (" ----------------------------\n")

create_database()

url = 'https://inmuebles.mercadolibre.com.ar/terrenos-lotes/venta/bsas-gba-norte/escobar/'

page_num = 1
index = 0
info = {}

while page_num != 0: #itera pagina por pagina

    soup = get_url(url, page_num)
    items = soup.find_all('li', attrs={'class': 'ui-search-layout__item'})

    for item in items:

        index += 1

        geographic_area = item.find('span', class_="ui-search-item__group__element ui-search-item__location")
        if geographic_area != None:
            geographic_area = geographic_area.text.strip()
        else:
            geographic_area = 'N/A'

        price_symbol = item.find('span', class_="price-tag-symbol")
        if price_symbol != None:
            price_symbol = price_symbol.text.strip()
        else:
            price_symbol = 'N/A'

        price = item.find('span', class_="price-tag-fraction")
        if price != None:
            price = price.text.strip()
            price = int(price.replace('.', ''))
        else:
            price = 'N/A'

        surface_description = item.find('li', class_="ui-search-card-attributes__attribute")
        if surface_description != None:
            surface_description = surface_description.text.strip()
        else:
            surface_description = 'N/A'

        if 'm²' in surface_description:
            surface_symbol = 'm2'
        elif 'ha' in surface_description:
            surface_symbol = 'ha'
        else:
            surface_symbol = 'N/A'

        surface = surface_description.replace(',','')
        surface = (re.findall('\d+', surface))

        if len(surface) == 1:
            surface_total = int(surface[0])
            surface_from = 0
            surface_to = 0
        elif len(surface) == 2:
            surface_total = 0
            surface_from = int(surface[0])
            surface_to = int(surface[1])
        else:
            surface_total = 'N/A'
            surface_from = 'N/A'
            surface_to = 'N/A'


        link = item.find('a', class_= 'ui-search-link')['href'],
        if link != None:
            link=  link[0]
        else:
            link = 'N/A'

#Appendea la data al dict info
        info[index] = [index, geographic_area, price_symbol, price, surface_description, surface_symbol, surface_from, surface_to, surface_total, link]


    if len(items) != 0: #para terminar o no el loop por pagina
        page_num = page_num + len(items)
    else:
        page_num = 0

print ('Loading info into database...\n')

ml_scrapper = sqlite3.connect('ml_scrapper.db')
cursor = ml_scrapper.cursor()

for item in info:

    ingreso = [(info[item][0], info[item][1], info[item][2], info[item][3], info[item][4], info[item][5], info[item][6], info[item][7], info[item][8], info[item][9])]
    cursor.executemany("INSERT INTO ESCOBAR VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", ingreso)

ml_scrapper.commit()
ml_scrapper.close()

print ('Info was loaded to the database successfully.\n')