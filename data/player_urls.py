import urllib.request
from bs4 import BeautifulSoup

# link = https://www.basketball-reference.com/players/(a-z)/
def get_players(link):
    url = link
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    table = 'players'
    rows = soup.find('table', attrs={'id': table }).find('tbody').find_all('tr')
