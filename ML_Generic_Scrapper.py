from create_database_generic import create_database
from web_retriever_generic import get_url
import sqlite3
import re

print ("\n ----------------------------")
print ("| Welcome to Mati's Scrapper |")
print (" ----------------------------\n")


data_base_name = input('Please input the name for the database you want to create to save the data in.\n'
                       '--->')
create_database(data_base_name)


search = input('What do you wish to scrap in MercadoLibre.com.ar?\n'
               '--->')

page_num = 1
index = 0
info = {}

while page_num != 0: #itera pagina por pagina

    soup = get_url(search, page_num)
    items = soup.find_all('li', attrs={'class': 'ui-search-layout__item'})

    for item in items:

        index += 1

        description = item.find('h2', class_="ui-search-item__title ui-search-item__group__element")
        if description != None:
            description = description.text.strip()
        else:
            description = 'N/A'

        original_price_symbol = item.find('span', class_="price-tag-symbol")
        if original_price_symbol != None:
            original_price_symbol = original_price_symbol.text.strip()
        else:
            original_price_symbol = 'N/A'

        original_price = item.find('span', class_="price-tag-fraction")
        if original_price != None:
            original_price = original_price.text.strip()
            original_price = int(original_price.replace('.', ''))
        else:
            original_price = 'N/A'

        discounted_price_symbol = item.find('span', class_="price-tag-symbol")
        if discounted_price_symbol != None:
            discounted_price_symbol = discounted_price_symbol.text.strip()
        else:
            discounted_price_symbol = 'N/A'

        discounted_price = item.find('span', class_="price-tag-fraction")
        if discounted_price != None:
            discounted_price = discounted_price.text.strip()
            discounted_price = int(discounted_price.replace('.', ''))
        else:
            discounted_price = 'N/A'

        discount_percentage = item.find('span', class_="ui-search-price__discount")
        if discount_percentage != None:
            discount_percentage = discount_percentage.text.strip()
        else:
            discount_percentage = 'N/A'

        type_of_delivery = item.find('div', class_="ui-search-item__highlight-label")
        if type_of_delivery != None:
            type_of_delivery = type_of_delivery.text.strip()
        else:
            type_of_delivery = 'N/A'

        date_of_arrival = item.find('span', class_="ui-search-item__promise__text ui-search-item__promise__text--long ui-search-item__promise__text--last")
        if date_of_arrival != None:
            date_of_arrival = date_of_arrival.text.strip()
        else:
            date_of_arrival = 'N/A'

        installments = item.find('span', class_="ui-search-item__group__element ui-search-installments ui-search-color--LIGHT_GREEN")
        if installments != None:
            installments = installments.text.strip()
        else:
            installments = 'N/A'

        link = item.find('a', class_= 'ui-search-link')['href'],
        if link != None:
            link=  link[0]
        else:
            link = 'N/A'

#Appendea la data al dict info
        info[index] = [index, description, original_price_symbol, original_price, discounted_price_symbol, discounted_price, discount_percentage, type_of_delivery, date_of_arrival, installments, link]


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