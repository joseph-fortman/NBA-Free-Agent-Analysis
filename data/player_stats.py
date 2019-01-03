import time
import urllib.request
from bs4 import BeautifulSoup

EXT = "https://www.basketball-reference.com"
table = "per_game"
year = "2018-19"

def create_CSV(urls):
    data = ""
    for name in urls:
        print(name + " " + EXT+urls[name])
        data += name + "," + get_table(EXT + urls[name])
        time.sleep(5)
    # write all contents
    fp = open("data/matrix.csv", 'w+')
    fp.write(data)
    fp.close()

    return

# get comma delimited text of per_game data for specified year
def get_table(player_url):
    url = player_url
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    # find the table rows
    rows = soup.find('table', attrs={'id': table }).find('tbody').find_all('tr')
    buffer = ""
    # traverse per_game data for relevent years
    for row in rows:
        temp = row.get_text(",") + "\n"
        if year in temp:
            buffer += temp

    return buffer
