
from scrape_total_pages import get_total_pages

import os
import requests
from bs4 import BeautifulSoup

site = 'https://id.jobstreet.com'
url = site + '/id/python-jobs'
#url = 'https://www.tokopedia.com'

def get_items(url):

    soup: BeautifulSoup = None

    # read from file
    with open('temp/page.html', 'r') as inputFile:
        content = inputFile.read()
        soup = BeautifulSoup(content, 'html.parser')
        #print(soup.prettify())

    if soup is None:

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive',
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200 :
            raise ConnectionError

        try:
            os.mkdir('temp')
        except:
            pass

        with open('temp/page.html', 'w') as outfile:
            outfile.write(response.text)

        soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all('article', '_1decxdv0')

    print('================================')

    job_list = []
    for item in items:
        #job_title = item.find('a', {'data-automation':'jobTitle'})
        job_title = item.find('h3')
        _job_title = job_title.text

        #if job_title is None:
        #    print(item)

        company = item.find('a', {'data-automation':'jobCompany'})
        #print(company.text)
        if company :
            _company_name = company.text
            try:
                _company_link = site + company['href']
            except:
                _company_link = '-'
        else:
            _company_name = '-'
            _company_link = '-'
            #print(job_title.text)
            #print(item.prettify())
            """company = item.find('span', {'class':'_1decxdv0'})
            if company :
                print(company.text)
            else:
                print(item.prettify())"""

        locations = item.find_all('span', {'data-automation':'jobCardLocation'})
        if len(locations) > 1:
            _company_address = locations[0].text + locations[1].text
        else:
            _company_address = locations[0].text

        # data sorting
        data_dict = {
            'title' : _job_title,
            'company_name' : _company_name,
            'link' : _company_link,
            "address" : _company_address,
        }

        job_list.append( data_dict)

    print(job_list)


if __name__ == '__main__':
    get_items(url)
    #total_pages = get_total_pages(url)
    #print(total_pages)