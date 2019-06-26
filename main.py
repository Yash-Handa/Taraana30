"""
The script produces a data folder with all the .csv files
the .csv files contain data from sites:
radiomirchi.com, gaana.com, hungama.com, jiosaavn.com, wynk.in
and a final.csv that contain a list of top 30 songs from all providers
"""
import csv
import os
from multiprocessing.pool import ThreadPool
from scrapers import wynk, saavn, mirchi, hungama, gaana
from utils.week_calc import saturday

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

for func in FUNC_LIST:
    thread = POOL.apply_async(func)
    THREADS.append(thread)

for thread in THREADS:
    result = thread.get()
    headers = list(result[0].keys())
    file_path = os.path.join(FOLDER_PATH, result[0].get('provider') + '.csv')
    with open(file_path, 'w', encoding="utf-8", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)
        for song in result:
            csvwriter.writerow(list(song.values()))
