"""
A web scraper to scrap mirchi top 20 songs of the week
the content is updated on saturday
"""
import html as htm
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

URL = 'http://www.radiomirchi.com/more/mirchi-top-20/'


def get_data(url, headers):
    """
    Request the mirchi server for data and
    return the HTML page of the top 20 songs
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


def top_20(html):
    '''
    takes HTML page of songs and return a sanitized list of the songes
    '''
    if not html:
        return None
    html = htm.unescape(html)
    final = []
    soup = Soup(html, 'lxml')
    collector = soup.find_all('div', class_='pannel02')
    if len(collector) != 20:
        return None

    for s_html in collector:
        video = str(s_html.contents[1].a['href'])
        if video[0] == '#':
            video = str(s_html.contents[1].a.img['data-vid-src'])
            video = 'https:' + video.replace('embed/', 'watch?v=')
        final.append({
            'video': video,
            'title': str(s_html.contents[3].h2.get_text()),
            'album': str(s_html.contents[3].h3.get_text().split('\n')[0]),
            'info': str(s_html.contents[5].get_text().strip()),
            'provider': 'mirchi'
        })
    return final


def mirchi():
    """
    The main function to be exported
    which retruns the list of top 20 bollywood songs from Mirchi
    """
    return top_20(get_data(URL, HEADERS))


if __name__ == '__main__':
    print(mirchi())
