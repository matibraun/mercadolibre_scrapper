from bs4 import BeautifulSoup
import requests

def get_url(web, page_number):

    url = web + f'_Desde_{page_number}'

    print (f'\nRetrieving the URL {url}.')

    url_raw = requests.get(url)
    print (f'\nThe URL {url} was retreived succesfuly.\n')
    url_processed = url_raw.text
    soup = BeautifulSoup(url_processed, 'html.parser')

    return soup