"""
A web scraper to scrap wynk Weekly Top 20 - Bollywood
THis uses the JSON object directly from wynk ;)
the content is updated on monday
"""
import requests
from bs4 import BeautifulSoup as soup

HEADERS = {
    'User-Agent':
    'Mozilla/5.0 (X11; Linux x86_64) '
    'AppleWebKit/537.11 (KHTML, like Gecko) '
    'Chrome/23.0.1271.64 Safari/537.11',
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset':
    'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding':
    'none',
    'Accept-Language':
    'en-US,en;q=0.8',
    'Connection':
    'keep-alive'
}

# https://content.wynk.in/music/v3/content?id=srch_bsb_1491818945339&type=PLAYLIST&count=50&offset=0
URL = 'https://content.wynk.in/music/v3/content'
PARAMS = {
    'id': 'srch_bsb_1491818945339',
    'type': 'PLAYLIST',
    'count': '50',
    'offset': '0'
}
RESPONSE = requests.get(URL, headers=HEADERS, params=PARAMS)
WYNK = RESPONSE.json()
print(WYNK)
