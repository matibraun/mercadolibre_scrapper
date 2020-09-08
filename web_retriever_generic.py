from bs4 import BeautifulSoup
import requests

def get_url(search, page_num):

    url_temp = 'https://listado.mercadolibre.com.ar/' + f'{search.replace(" ", "-")}#D[A:{search.replace(" ", "%20")}]'

    print (f'\nRetrieving the URL {url_temp}.')

    url_raw_temp = requests.get(url_temp)
    print (f'\nThe URL {url_temp} was retreived succesfuly.\n')
    url_processed_temp = url_raw_temp.text
    soup_temp = BeautifulSoup(url_processed_temp, 'html.parser')
    link = soup_temp.find('a', class_='andes-pagination__link ui-search-link')['href'],

    url = link[0] + f'_Desde_{page_num}'

    print(f'\nRetrieving the URL {url}.')

    url_raw = requests.get(url)
    print(f'\nThe URL {url} was retreived succesfuly.\n')
    url_processed = url_raw.text
    soup = BeautifulSoup(url_processed, 'html.parser')

    return soup