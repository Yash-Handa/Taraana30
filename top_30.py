"""
The script to calculate the top 30 songs
and all the candidate songs of the week
and write them to top_30.csv and candidates.csv
Not to be run directly
"""
import hashlib
import csv
from os import path
from utils.sanitizer import sanitizer


def top_30(all_data, folder_path):
    """
    the main funtion to be called, will write 2 .csv file with data
    """
    all_songs = []
    songs = set()
    for provider in all_data:
        for i, song in enumerate(provider):
            title = sanitizer(song.get('title'))
            song_id = str(hashlib.md5(title.encode()).hexdigest())
            # song_id = title
            # the song already exist in the all_songs list
            if title in songs:
                song_dict = list(
                    filter(lambda song: song['id'] == song_id, all_songs))[0]
                new_song_dict = eval(  # pylint: disable=W0123
                    song.get('provider') + '(song_dict, song, i)')
                all_songs[all_songs.index(song_dict)] = new_song_dict
            else:
                songs.add(title)
                all_songs.append(
                    eval(  # pylint: disable=W0123
                        song.get('provider') +
                        "({'id': song_id, 'points': 0}, song, i)"))
    create_files(folder_path, all_songs)


def hungama(song_dict, hungama_song, i):
    """
    this function adds details from gaana server for a particular song
    """
    song_dict['hungama_url'] = hungama_song.get('shortUrl')
    song_dict['lyricist'] = hungama_song.get('lyricist')
    song_dict['image_200'] = hungama_song.get('image_200')
    if i <= 29:
        song_dict['points'] += 30 - i
    if not song_dict.get('title'):
        song_dict['title'] = hungama_song.get('title').title()
    if not song_dict.get('album'):
        song_dict['album'] = hungama_song.get('album').title()
    if not song_dict.get('image'):
        song_dict['image'] = hungama_song.get('image_200')
    if not song_dict.get('keywords'):
        song_dict['keywords'] = hungama_song.get('keywords')
    else:
        song_dict['keywords'] = song_dict['keywords'] | hungama_song.get(
            'keywords')
    return song_dict


def mirchi(song_dict, mirchi_song, i):
    """
    this function adds details from mirchi server for a particular song
    """
    song_dict['video'] = mirchi_song.get('video')
    song_dict['info'] = mirchi_song.get('info')
    if i <= 29:
        song_dict['points'] += 30 - i
    if not song_dict.get('title'):
        song_dict['title'] = mirchi_song.get('title').title()
    if not song_dict.get('album'):
        song_dict['album'] = mirchi_song.get('album').title()
    return song_dict


def wynk(song_dict, wynk_song, i):
    """
    this function adds details from wynk server for a particular song
    """
    song_dict['wynk_url'] = wynk_song.get('shortUrl')
    song_dict['contentLang'] = wynk_song.get('contentLang')
    if i <= 29:
        song_dict['points'] += 30 - i
    if not song_dict.get('title'):
        song_dict['title'] = wynk_song.get('title').title()
    if not song_dict.get('album'):
        song_dict['album'] = wynk_song.get('album').title()
    if not song_dict.get('duration'):
        song_dict['duration'] = wynk_song.get('duration')
    if not song_dict.get('label'):
        song_dict['label'] = wynk_song.get('label')
    if not song_dict.get('image'):
        song_dict['image'] = wynk_song.get('image_320')
    if not song_dict.get('keywords'):
        song_dict['keywords'] = wynk_song.get('keywords')
    else:
        song_dict['keywords'] = song_dict['keywords'] | wynk_song.get(
            'keywords')
    if not song_dict.get('singers'):
        song_dict['singers'] = wynk_song.get('singers')
    else:
        song_dict['singers'] = song_dict['singers'] | wynk_song.get('singers')
    return song_dict


def saavn(song_dict, saavn_song, i):
    """
    this function adds details from saavn server for a particular song
    """
    song_dict['saavn_url'] = saavn_song.get('shortUrl')
    song_dict['label'] = saavn_song.get('label')
    song_dict['music'] = saavn_song.get('music')
    if i <= 29:
        song_dict['points'] += 30 - i
    if not song_dict.get('title'):
        song_dict['title'] = saavn_song.get('title').title()
    if not song_dict.get('album'):
        song_dict['album'] = saavn_song.get('album').title()
    if not song_dict.get('duration'):
        song_dict['duration'] = saavn_song.get('duration')
    if not song_dict.get('contentLang'):
        song_dict['contentLang'] = saavn_song.get('contentLang')
    if not song_dict.get('release'):
        song_dict['release'] = saavn_song.get('year')
    if not song_dict.get('keywords'):
        song_dict['keywords'] = saavn_song.get('keywords')
    else:
        song_dict['keywords'] = song_dict['keywords'] | saavn_song.get(
            'keywords')
    if not song_dict.get('singers'):
        song_dict['singers'] = saavn_song.get('singers')
    else:
        song_dict['singers'] = song_dict['singers'] | saavn_song.get('singers')
    return song_dict


def gaana(song_dict, gaana_song, i):
    """
    this function adds details from gaana server for a particular song
    """
    song_dict['gaana_url'] = gaana_song.get('shortUrl')
    song_dict['duration'] = gaana_song.get('duration')
    song_dict['album'] = gaana_song.get('album').title()
    song_dict['title'] = gaana_song.get('title').title()
    song_dict['image'] = gaana_song.get('image_400')
    song_dict['image_800'] = gaana_song.get('image_800')
    song_dict['release'] = gaana_song.get('release_date')
    if i <= 29:
        song_dict['points'] += 30 - i
    if not song_dict.get('contentLang'):
        song_dict['contentLang'] = gaana_song.get('contentLang')
    if not song_dict.get('singers'):
        song_dict['singers'] = gaana_song.get('singers')
    else:
        song_dict['singers'] = song_dict['singers'] | gaana_song.get('singers')
    return song_dict


def create_files(folder_path, data):
    """
    the function to create .csv file with all the data (candidates.csv)
    and top_30.csv file
    """
    headers = [
        'id', 'title', 'album', 'duration', 'release', 'label', 'points',
        'contentLang', 'singers', 'music', 'lyricist', 'info', 'image_200',
        'image', 'image_800', 'video', 'gaana_url', 'saavn_url',
        'wynk_url', 'hungama_url'
    ]
    with open(path.join(folder_path, 'candidates.csv'),
              'w',
              encoding="utf-8",
              newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)
        for song in data:
            song_data = []
            for key in headers:
                if song.get(key):
                    song_data.append(song.get(key))
                else:
                    song_data.append('')
            csvwriter.writerow(song_data)

    def points_func(song):
        # fields with value 0 are left blank in .csv files
        if not song.get('points'):
            return 0
        return int(song.get('points'))

    top_30_songs = sorted(data, key=points_func, reverse=True)[:30]
    headers_top_30 = [
        'id', 'title', 'album', 'duration', 'release', 'label', 'points',
        'singers', 'music', 'lyricist', 'image'
    ]

    with open(path.join(folder_path, 'top_30.csv'),
              'w',
              encoding="utf-8",
              newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers_top_30)
        for song in top_30_songs:
            song_data = []
            for key in headers_top_30:
                if song.get(key):
                    song_data.append(song.get(key))
                else:
                    song_data.append('')
            csvwriter.writerow(song_data)
