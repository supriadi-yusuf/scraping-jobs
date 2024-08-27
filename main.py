
from scrape_total_pages import get_total_pages

url = 'https://id.jobstreet.com/id/python-jobs'
#url = 'https://www.tokopedia.com'

if __name__ == '__main__':
    total_pages = get_total_pages(url)
    print(total_pages)