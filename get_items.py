import pandas as pd
import requests
from bs4 import BeautifulSoup


import json
import os


def get_items(url, query='', location='', page=''):

    soup: BeautifulSoup = None

    # read from file
    try:
        with open(f'temp/page-{query}-{location}-{page}.html', 'r') as inputFile:
            content = inputFile.read()
            soup = BeautifulSoup(content, 'html.parser')
            #print(soup.prettify())
    except FileNotFoundError:
        pass

    if soup is None:

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive',
        }

        if query:
            url = f'{url}/id/{query}'

            if location:
                url = f'{url}/{location}'

            if page:
                url=f'{url}?page={page}'

        response = requests.get(url, headers=headers)
        if response.status_code != 200 :
            raise ConnectionError

        try:
            os.mkdir('temp')
        except FileExistsError:
            pass

        with open(f'temp/page-{query}-{location}-{page}.html', 'w') as outfile:
            outfile.write(response.text)

        soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all('article', {'data-automation':'normalJob'})

    print('================================')

    site = 'https://id.jobstreet.com'
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

    return job_list

