import json
import time
import urllib.request
from bs4 import BeautifulSoup
from string import ascii_lowercase

EXT = "https://www.basketball-reference.com/players/"
table = "players"

# Update URLs for players who were playing, injured, or available during a
# specified year.
def update_URLs(year):
    player_urls = {}
    for letter in ascii_lowercase:
        if (letter != "x"):
            abc = EXT + letter + '/'
            player_urls.update(get_players(abc, year))
            time.sleep(5)

    fp = open("data/urls.json", 'w+')
    json.dump(player_urls, fp, indent=2)

# abc = https://www.basketball-reference.com/players/(a-z)/
def get_players(abc, year):
    page = urllib.request.urlopen(abc)
    soup = BeautifulSoup(page, 'html.parser')
    rows = soup.find('table', attrs={'id': table }).find('tbody').find_all('tr')

    # start by returning all rows with 2019 specified
    buffer = {}
    for row in rows:
        temp = row.get_text(",") + "\n"
        if year in temp:
            a = row.find('a', href=True)
            buffer[a.get_text()] = a['href']
            print(a.get_text() + " " + buffer[a.get_text()])

    return buffer
