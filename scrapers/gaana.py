"""A web scraper to scrap gaana Bollywood Top 50 playlist"""
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

URL = 'https://gaana.com/playlist/gaana-dj-bollywood-top-50-1'


def get_data(url, headers):
    """
    Request the gaana server for data and
    return the HTML page of the top 50 songs
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


def top_50(html):
    '''
    takes HTML page of songs and return a sanitized list of the songes
    '''
    if not html:
        return None
    final = []
    soup = Soup(html, 'lxml')
    collector = soup.find_all('span', attrs={'data-type': 'playSong'})
    if len(collector) != 50:
        return None

    for s_html in collector:
        song = json.loads(str(s_html.string))
        s_detail = {
            'duration': song.get('duration'),
            'title': song.get('title').strip(),
            'album': song.get('albumtitle').strip(),
            'image_200': song.get('atw'),
            'image_400': song.get('atw').replace('size_m_', 'size_l_'),
            'image_800': song.get('atw').replace('size_m_', 'size_xl_'),
            'shortUrl': 'https://gaana.com' + song.get('share_url'),
            'contentLang': song.get('language').strip().lower()[:2],
            'release_date': song.get('release_date'),
            'gaana_id': song.get('id'),
            # 'singers': set(song.get('singers').split(', ')),
            'provider': 'gaana'
        }

        s_detail['singers'] = set()
        for artist in song.get('artist').split(','):
            s_detail['singers'].add(
                artist.split('###')[0].strip().replace('-', ' ').title())

        final.append(s_detail)
    return final


def gaana():
    """
    The main function to be exported
    which retruns the list of top 50 bollywood songs from Gaana
    """
    return top_50(get_data(URL, HEADERS))


if __name__ == '__main__':
    print(gaana())
