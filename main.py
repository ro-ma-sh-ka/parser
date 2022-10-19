import requests
from bs4 import BeautifulSoup


def get_html(url: str) -> requests.models.Response:
    """the function gets html to send it to get_content function"""
    r = requests.get(url)
    return r


def get_content(html: requests.models.Response) -> str:
    """the function takes html from get_html function uses BeautifulSoup to get current weather forecast"""
    soup = BeautifulSoup(html.content, 'html.parser')
    for meta in soup.findAll('meta', {'name': 'description'}):
        weather = meta['content']
    return weather
