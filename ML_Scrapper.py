from create_database import create_database
from web_retriever import get_url
from bs4 import BeautifulSoup


print ("\n ----------------------------")
print ("| Welcome to Mati's Scrapper |")
print (" ----------------------------\n")

create_database()

url = 'https://inmuebles.mercadolibre.com.ar/terrenos-lotes/venta/bsas-gba-norte/escobar/'

page_num = 1

soup = get_url(url, page_num)

print (soup)