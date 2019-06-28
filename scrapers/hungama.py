"""
A web scraper to scrap hungama Bollywood Top 40
THis uses the JSON object directly from hungama ;)
"""
import urllib.parse
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

# https://www.hungama.com/audio-player-data/playlist/6532?_country=IN
URL = 'https://www.hungama.com/audio-player-data/playlist/6532'
PARAMS = {'_country': 'IN'}


def get_data(url, headers, params):
    """
    Request the hungama server for data and
    return the HTML page of the top 40 songs
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
        return response.json()


def top_40(raw):
    '''
    takes unsanitised list of songs and return a sanitized version
    '''
    if not raw:
        return None
    final = []

    for song in raw:
        s_detail = {
            'title': song.get('song_name').strip().replace(' (From', ''),
            'image_200': song.get('img_src'),
            'album': song.get('album_name').strip(),
            # set is created from a list with only one element
            'lyricist': set([song.get('lyricist').split(',')[0].strip()]),
            'hungama_id': song.get('mediaid'),
            'provider': 'hungama',
            'singers': {x.strip().replace('-', ' ').title()
                        for x in song.get('singer_name').split(', ')}
        }

        link = 'https://www.hungama.com/song/'
        link += urllib.parse.quote_plus(s_detail['title'].lower()) \
            .replace('+', '-') + '/' + str(s_detail['hungama_id']) + '/'
        s_detail['shortUrl'] = link

        s_detail['keywords'] = s_detail['singers'] | s_detail['lyricist'] \
            | set([s_detail['title'], s_detail['album']])

        if s_detail['title'] + ' (From "' in s_detail['album']:
            s_detail['album'] = s_detail['album'].split('"')[1]

        final.append(s_detail)
    return final


def hungama():
    """
    The main function to be exported
    which retruns the list of top 40 bollywood songs from Hungama
    """
    return top_40(get_data(URL, HEADERS, PARAMS))


if __name__ == '__main__':
    print(hungama())
