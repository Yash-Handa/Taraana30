"""
The script produces a data folder with all the .csv files
the .csv files contain data from sites:
radiomirchi.com, gaana.com, hungama.com, jiosaavn.com, wynk.in
and a final.csv that contain a list of top 30 songs from all providers
"""
import csv
import os
from sys import argv
from multiprocessing.pool import ThreadPool
from scrapers import wynk, saavn, mirchi, hungama, gaana
from utils.week_calc import saturday
from top_30 import top_30

FOLDER_PATH = os.path.join('data', saturday())
try:
    os.makedirs(FOLDER_PATH)
except FileExistsError:
    pass

FUNC_LIST = [
    wynk.wynk, saavn.saavn, mirchi.mirchi, hungama.hungama, gaana.gaana
]
POOL = ThreadPool(processes=5)  # 5 threads
THREADS = []
RESULTS = []
ALL = '--all' in argv or '-a' in argv

for func in FUNC_LIST:
    thread = POOL.apply_async(func)
    THREADS.append(thread)

for thread in THREADS:
    result = thread.get()
    if ALL:
        headers = list(result[0].keys())
        file_path = os.path.join(FOLDER_PATH,
                                 result[0].get('provider') + '.csv')
        with open(file_path, 'w', encoding="utf-8", newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(headers)
            for song in result:
                csvwriter.writerow(list(song.values()))
    RESULTS.append(result)

# calculte top 30 songs & write candidates and final top_30 songs in .csv files
top_30(RESULTS, FOLDER_PATH)
