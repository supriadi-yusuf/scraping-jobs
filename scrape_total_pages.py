import requests
from bs4 import BeautifulSoup


import os


def get_total_pages(url):

    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise SystemError

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(response.text)

    #scraping step
    soup = BeautifulSoup(response.text, 'html.parser')

    pagination = soup.find('ul', '_1decxdv0 _1decxdv3 _110qf3s5a _110qf3sfq')

    pages = pagination.find_all('li')

    page_list = [page.text for page in pages if page.text.isnumeric()]

    total_page = int(max(page_list))

    return total_page