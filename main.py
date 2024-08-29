
from get_items import get_items
from scrape_total_pages import get_total_pages


site = 'https://id.jobstreet.com'
url = site + '/id/python-jobs'
if __name__ == '__main__':
    get_items(url)
    #total_pages = get_total_pages(url)
    #print(total_pages)