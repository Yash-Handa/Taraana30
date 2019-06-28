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


def taraana30(all_files=False):
    """
    The main function to be exported wheen using as module
    it will just write the files will not return any thing
    """
    folder_path = os.path.join(os.getcwd(), 'data', saturday())
    try:
        os.makedirs(folder_path)
    except FileExistsError:
        pass

    func_list = [
        wynk.wynk, saavn.saavn, mirchi.mirchi, hungama.hungama, gaana.gaana
    ]
    pool = ThreadPool(processes=5)  # 5 threads
    threads = []
    results = []
    all_csv = '--all' in argv or '-a' in argv or all_files

    for func in func_list:
        thread = pool.apply_async(func)
        threads.append(thread)

    for thread in threads:
        result = thread.get()
        if all_csv:
            headers = list(result[0].keys())
            file_path = os.path.join(folder_path,
                                     result[0].get('provider') + '.csv')
            with open(file_path, 'w', encoding="utf-8", newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(headers)
                for song in result:
                    csvwriter.writerow(list(song.values()))
        results.append(result)

    # calculte top 30 songs & write candidates and final top_30 songs in
    #  .csv files
    top_30(results, folder_path)


if __name__ == '__main__':
    taraana30()
