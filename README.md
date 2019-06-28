[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/Yash-Handa/Taraana30.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Yash-Handa/Taraana30/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Yash-Handa/Taraana30.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Yash-Handa/Taraana30/context:python)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Yash-Handa/Taraana30.svg)
![GitHub](https://img.shields.io/github/license/Yash-Handa/Taraana30.svg)

# Taraana30

A web scraper that calculates weekly Top 30 Bollywood Songs from various platforms:

- **Radio Mirchi** - [List](http://www.radiomirchi.com/more/mirchi-top-20/)
- **Gaana** - [Play List](https://gaana.com/playlist/gaana-dj-bollywood-top-50-1)
- **saavn** - [Play List](https://www.jiosaavn.com/featured/weekly-top-songs/8MT-LQlP35c_)
- **Hungama** - [Play List](https://www.hungama.com/playlists/bollywood-top-40/6532/)
- **Wynk** - [Play List](https://wynk.in/music/playlist/weekly-top-20-bollywood/bb_1491818945339)

The Web Scraper scrapes the above List/Play List for the data from various providersand save the data in the data folder : `./data/<date of previous week's saturday>/` more on `<date of previous week's saturday>` later

### Usage

The Web Scraper provides 2 main commands:

1. To get just top_30.csv and candidates.csv:
```shell
$ python main.py
```
 Run the above command from the root of the folder to produce `top_30.csv` and `candidates.csv` files in the data folder: `./data/<date of previous week's saturday>/top_30.csv` and `/candidates.csv`

 2. To get all .csv files from the scraper:
 ```shell
 $ python main.py --all
 ```
Run the above command from the root of the folder to procude:
- `candidates.csv`
- `top_30.csv`
- `gaana.csv`
- `hungama.csv`
- `mirchi.csv`
- `saavn.csv`
- `wynk.csv`

in the `./data/<date of previous week's saturday>/` folder if it exist or create it then create the files


**`<date of previous week's saturday>`**: The folder naming system of the scraper uses the date of the previous Saturday to distinguise between two weeks. The date is in the formate: `DD-MM-YYYY`. (The week changes on `Sunday 00:00:00` i.e., even if the scrip is run on Saturday the folder name will be the date of previous Saturday)

Example:
```
./
├── data
    ├── 22-06-2019
    │   ├── top_30.csv
    │   └── candidates.csv
    └── 29-06-2019
        ├── top_30.csv
        ├── candidates.csv
        ├── gaana.csv
        ├── hungama.csv
        ├── mirchi.csv
        ├── saavn.csv
        └── wynk.csv
```

### Installation

Currently the tool is only present as a GitHub repository and could be used from there only
1. Fork and Clone to your machine
2. Run the pipenv: `pipenv shell`
3. run `pipenv install --ignore-pipfile` to install all dependancies to your machine. The main dependancies are:
   - beautifulsoup4
   - requests
   - lxml

### Technical Aspects:
- Langauge: **Python v3.7.3**
- Scraping Module: **BeautifulSoup v4.7.1** with **lxml parser**
- I/O request Module: **requests v2.22.0**
- Misc: This project is a collection of 5 scrapers one for each plateform:
  - `radiomirchi.com`
  - `gaana.com`
  - `hungama.com`
  - `jiosaavn.com`
  - `wynk.in`

  To speed up the scraping process particularly the delay in various I/O requests for gathering the source code from various platforms **Multi-Theading** is used, 1 thread per scraper (i.e., thread pool of 5 threads)

<p align="center"><br><br>
  <img alt="kitten" src="https://media.giphy.com/media/t7MWRoExDRF72/giphy.gif">
</p>