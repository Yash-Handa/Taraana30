"""A web scraper to scrap saavn Weekly Top 15 Songs"""
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

URL = 'https://www.jiosaavn.com/featured/weekly-top-songs/8MT-LQlP35c_'
RESPONSE = requests.get(URL, headers=HEADERS)
SAAVN = RESPONSE.text
print(SAAVN)
