from create_database import create_database
from web_retriever import get_url

print ("\n ----------------------------")
print ("| Welcome to Mati's Scrapper |")
print (" ----------------------------\n")

create_database()

url = 'https://inmuebles.mercadolibre.com.ar/terrenos-lotes/venta/bsas-gba-norte/escobar/'

page_num = 1
index = 0

soup = get_url(url, page_num)

for item in soup.find_all('li', attrs={'class': 'ui-search-layout__item'}):

    index += 1
    print (index)

    geographic_area = item.find('span', class_="ui-search-item__group__element ui-search-item__location")
    if geographic_area != None:
        print (geographic_area.text.strip())
    else:
        geographic_area = 'N/A'
        print (geographic_area)

    price_symbol = item.find('span', class_="price-tag-symbol")
    if price_symbol != None:
        print (price_symbol.text.strip())
    else:
        price_symbol = 'N/A'
        print (price_symbol)

    price = item.find('span', class_="price-tag-fraction")
    if price != None:
        print (price.text.strip())
    else:
        price = 'N/A'
        print (price)

    surface = item.find('li', class_="ui-search-card-attributes__attribute")
    if surface != None:
        print (surface.text.strip())
    else:
        surface = 'N/A'
        print (surface)

    link = item.find('a', class_= 'ui-search-link')['href'],
    if link != None:
        print (link[0])
    else:
        link = 'N/A'
        print (link)