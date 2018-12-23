import urllib.request
from bs4 import BeautifulSoup

# table may be consistent. SportsReference effectively blocks scraping any tables
# other than player averages.
def get_table(player_url, table):
    url = player_url
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    # find the table rows
    rows = soup.find('table', attrs={'id': table }).find('tbody').find_all('tr')
    buffer = ""

    for row in rows:
        buffer += row.get_text(",") + "\n"

    return buffer
