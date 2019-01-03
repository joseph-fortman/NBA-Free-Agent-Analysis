import urllib.request
from bs4 import BeautifulSoup

def create_CSV(urls):
    table = "per_game"
    year = "2017-18"
    data = ""
    for name in urls:
        print(name + " " + urls[name])
        data += name + "," + get_table(urls[name], table, year)
    # write all contents
    fp = open("data/matrix.csv", 'w+')
    fp.write(data)
    fp.close()

    return

# get comma delimited text of per_game data for specified year
def get_table(player_url, table, year):
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
