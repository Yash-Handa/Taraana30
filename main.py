"""
The script produces a data folder with all the .csv files
the .csv files contain data from sites:
radiomirchi.com, gaana.com, hungama.com, jiosaavn.com, wynk.in
and a final.csv that contain a list of top 30 songs from all providers
"""
import csv
from scrapers import wynk, saavn, mirchi, hungama, gaana
from utils.week_calc import saturday

FOLDER_PATH = 'data/' + saturday() + '/'
