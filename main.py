import os
import pandas as pd
import json

from get_items import get_items
from scrape_total_pages import get_total_pages

def store_data(data):
    # create json
    try:
        os.mkdir('json_results')
    except FileExistsError:
        pass

    with open('json_results/job_list.json', 'w') as outFile:
        json.dump(data, outFile)

    try:
        os.mkdir('data_results')
    except FileExistsError:
        pass

    # create csv dan excel
    df = pd.DataFrame(data) # create data frame
    df.to_csv('data_results/job_lists.csv', index=False) # store to csv file
    df.to_excel('data_results/job_lists.xlsx', index=False) # store to xlsx file

def proses_scraping(url, query='', location=''):
    total_pages = get_total_pages(url, query, location)

    data = []
    for page in range(total_pages):
        data += get_items(url, query, location, page+1)

    store_data(data)

site = 'https://id.jobstreet.com'
url = site # + '/id/python-jobs'

if __name__ == '__main__':
    #get_items(url)
    #total_pages = get_total_pages(url, 'python-jobs', 'in-Banten')
    #print(total_pages)
    proses_scraping(url, 'python-jobs', 'in-Banten')

# https://id.jobstreet.com/id/python-jobs/in-Banten?page=3
# https://id.jobstreet.com/id/python-jobs?page=2
# https://id.jobstreet.com/id/python-jobs