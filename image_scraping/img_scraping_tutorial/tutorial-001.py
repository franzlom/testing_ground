"""
Using tutorial: https://www.youtube.com/watch?v=XVv6mJpFOb0

motivation: I want to scrape chrono24 for prices of watch over time and see if I can build a data base of watch prices overtime

By Franz Lomibao
"""
import unicodedata

import requests
from bs4 import BeautifulSoup

base_url = 'https://www.chrono24.co.nz'  # site to scrape
site = 'https://www.chrono24.co.nz/iwc/'  # site to scrape


def run():
    html_text = requests.get(site).text

    soup = BeautifulSoup(html_text, 'lxml')
    watch = soup.find('div', class_='article-item-container wt-search-result')  # this returns class bs4.element.Tag
    watch_name = watch.find('div', class_='article-title').text.strip()
    watch_price = watch.find('strong', class_=None).text
    watch_image = watch.find('img')['src']
    print(f'watch_name = {watch_name}')
    print(f'watch_image = {watch_image}')
    print(f'watch_price = {watch_price}')
    print('------------------------------')
    print(watch)


def run_two():
    html_text = requests.get(site).text

    soup = BeautifulSoup(html_text, 'lxml')
    watch_lst = soup.findAll('div',
                             class_='article-item-container wt-search-result')  # this returns class bs4.element.Tag

    output_lst = list()

    for watch in watch_lst:
        inner_dct = dict()
        # print(watch)
        watch_name = watch.find('div', class_='article-title').text.strip()
        watch_price = unicodedata.normalize('NFKD', watch.find('strong', class_=None).text).replace('\n', '')
        price_currency = watch_price.split('$')[0]
        try:
            watch_image = watch.find('img')['srcset'].split(' ')[0]
        except KeyError:
            watch_image = watch.find('img')['src'].split(' ')[0]

        watch_description = watch.find('img')['alt']
        chrono_url = watch.find('a')['href']

        watch_price = watch_price.split(' ')[-1]

        inner_dct['watch_name'] = watch_name
        inner_dct['watch_price'] = watch_price
        inner_dct['price_currency'] = price_currency
        inner_dct['watch_image'] = watch_image
        inner_dct['watch_description'] = watch_description
        inner_dct['chrono_url'] = f'{base_url}{chrono_url}'

        print(inner_dct)

        output_lst.append(inner_dct)

    return output_lst


if __name__ == '__main__':
    watch_info = run_two()

    print(watch_info)
