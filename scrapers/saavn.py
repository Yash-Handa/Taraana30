"""
A web scraper to scrap saavn Weekly Top 15 Songs
It actually have 30 songs
"""
import json
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup as Soup

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


def get_data(url, headers):
    """
    Request the saavn server for data and
    return the HTML page of the top 30 songs
    """
    response = ''
    try:
        response = requests.get(url, headers=headers)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
    else:
        return response.text


def top_30(html):
    '''
    takes HTML page of songs and return a sanitized list of the songes
    '''
    if not html:
        return None
    final = []
    soup = Soup(html, 'lxml')
    collector = soup.find_all('div', class_='hide song-json')
    if len(collector) != 30:
        return None

    for s_html in collector:
        song = json.loads(str(s_html.string))
        s_detail = {
            'duration': song.get('duration'),
            'title': song.get('title'),
            'album': song.get('album'),
            'image_150': song.get('image_url'),
            'shortUrl': song.get('tiny_url'),
            'label': song.get('label'),
            'contentLang': song.get('language').lower()[:2],
            'year': song.get('year'),
            'saavn_id': song.get('e_songid'),
            'singers': set(song.get('singers').split(', ')),
            'music': set(song.get('music').split(', ')),
            'provider': 'saavn'
        }
        prep = s_detail['singers'] | s_detail['music']
        prep_2 = set([s_detail['title'], s_detail['album'], s_detail['label']])
        s_detail['keywords'] = prep | prep_2
        final.append(s_detail)
    return final


def saavn():
    """
    The main function to be exported
    which retruns the list of top 30 bollywood songs from Saavn
    """
    return top_30(get_data(URL, HEADERS))


if __name__ == '__main__':
    print(saavn())
