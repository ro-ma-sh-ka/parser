import requests
from bs4 import BeautifulSoup


def get_html():
    url = "https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B5_(%D0%92%D0%94%D0%9D%D0%A5)"
    r = requests.get(url)
    return r


def get_content(html):
    soup = BeautifulSoup(html.content, 'html.parser')

    for meta in soup.findAll('meta', {'name': 'description'}):
        weather = meta['content']

    return print(weather)


html = get_html()
get_content(html)
