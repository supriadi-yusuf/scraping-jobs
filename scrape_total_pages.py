import requests
from bs4 import BeautifulSoup


import os


def get_total_pages(url, query=None, location=None):

    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    }

    if query:
        url = f'{url}/id/{query}'

        if location:
            url = '{}/{}'.format(url, location)

    #print(url)
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise SystemError

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w') as outfile:
        outfile.write(response.text)

    #scraping step
    soup = BeautifulSoup(response.text, 'html.parser')

    pagination = soup.find('nav', {'aria-label':'Penomoran halaman hasil'})

    # find all tag li in the element
    pages = pagination.find_all('li')

    page_list = [page.text for page in pages if page.text.isnumeric()]

    total_page = int(max(page_list))

    return total_page