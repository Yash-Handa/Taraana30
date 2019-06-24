"""
A web scraper to scrap wynk Weekly Top 20 - Bollywood
THis uses the JSON object directly from wynk ;)
the content is updated on monday
"""
import requests
from requests.exceptions import HTTPError

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


def get_data(url, headers, params):
    """
    Request the wynk server for data and return a list of the top 20 songs
    """
    response = ''
    try:
        response = requests.get(url, headers=headers, params=params)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
    else:
        return response.json()['items']


def top_20(raw):
    '''
    takes unsanitised list of songs and return a sanitized version
    '''
    if not raw:
        return None
    final = []
    for song in raw:
        s_detail = {
            'duration': song.get('duration'),
            'title': song.get('title'),
            'keywords': song.get('keywords'),
            'largeImage': song.get('largeImage').replace('320x180', '320x320'),
            'smallImage': song.get('smallImage'),
            'album': song.get('album'),
            'shortUrl': song.get('shortUrl'),
            'singer': song.get('subtitle').split(' - ')[0]
        }
        final.append(s_detail)
    return final


def wynk():
    """
    The main function to be exported
    which retruns the list of top 20 bollywood songs from Wynk
    """
    return top_20(get_data(URL, HEADERS, PARAMS))


if __name__ == '__main__':
    print(wynk())
