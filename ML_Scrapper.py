from create_database import create_database
from web_retriever import get_url

print ("\n ----------------------------")
print ("| Welcome to Mati's Scrapper |")
print (" ----------------------------\n")

create_database()

url = 'https://inmuebles.mercadolibre.com.ar/terrenos-lotes/venta/bsas-gba-norte/escobar/'

page_num = 1

soup = get_url(url, page_num)

for item in soup.find_all('li', attrs={'class': 'ui-search-layout__item'}):
    geographic_area = item.find('span', class_="ui-search-item__group__element ui-search-item__location")
    print (geographic_area.text.strip())

    price_symbol = item.find('span', class_="price-tag-symbol")
    print (price_symbol.text.strip())

    price = item.find('span', class_="price-tag-fraction")
    print (price.text.strip())

    surface = item.find('li', class_="ui-search-card-attributes__attribute")
    print (surface.text.strip())

    link = item.find('a', class_= 'ui-search-link')['href']
    print (link)