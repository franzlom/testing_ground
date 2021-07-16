"""
Using tutorial: https://www.youtube.com/watch?v=XVv6mJpFOb0

motivation: I want to scrape chrono24 for prices of watch over time and see if I can build a data base of watch prices overtime

By Franz Lomibao
"""
import asyncio
import time
import unicodedata

import aiohttp
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
        watch_name = watch.find('div', class_='article-title').text.strip()
        watch_price = unicodedata.normalize('NFKD', watch.find('strong', class_=None).text).replace('\n', '')
        price_currency = watch_price.split('$')[0]
        try:
            watch_image = watch.find('img')['srcset'].split(' ')[0]
        except KeyError:
            watch_image = watch.find('img')['data-srcset'].split(' ')[0]

        watch_description = watch.find('img')['alt']
        chrono_url = watch.find('a')['href']

        watch_price = watch_price.split(' ')[-1]

        inner_dct['watch_name'] = watch_name
        inner_dct['watch_price'] = watch_price
        inner_dct['price_currency'] = price_currency
        inner_dct['watch_image'] = watch_image
        inner_dct['watch_description'] = watch_description
        inner_dct['chrono_url'] = f'{base_url}{chrono_url}'

        output_lst.append(inner_dct)

    return output_lst


def scrape_site(html_lst):
    for html in html_lst:
        soup = BeautifulSoup(html, 'lxml')
        description = soup.findAll('span', id_='watchNotes')  # this returns class bs4.element.Tag

        description = description
        print(description)

        exit(-2)


async def fetch(session, url):
    async with session.get(url) as response:
        assert response.status == 200
        return await response.text()


async def get_more_data(url_lst):
    tasks = list()
    # url_lst = [
    #     'https://www.chrono24.co.nz/rolex/rolex-day-date-40--id19609982.htm',
    #     'https://www.chrono24.co.nz/rolex/rolex-submariner-kermit--id19741628.htm'
    # ]
    async with aiohttp.ClientSession() as session:
        for url in url_lst:
            task = asyncio.ensure_future(fetch(session, url))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)


        print(f'len(responses) = {len(responses)}')
        print(f'type(responses) = {type(responses)}')

        scrape_site(responses)


if __name__ == '__main__':
    start_time = time.time()
    # watch_info = run_two()
    # # async_stuff
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_more_data())

    search_response = run_two()
    print(search_response)

    watch_sites = [x['chrono_url'] for x in search_response]
    print('watch_site =')
    print(watch_sites)

    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(get_more_data(watch_sites))
    loop.run_until_complete(future)

    print("--- %s seconds ---" % (time.time() - start_time))
