import time
import urllib.request
from bs4 import BeautifulSoup

EXT = "https://www.basketball-reference.com"
table = "per_game"
year = "2018-19"

def group_CSV(urls):
    # get permission to write
    fp = open("data/group.csv", 'w+')
    # obtain data
    data = ""
    for name in urls:
        print(name + " " + EXT+urls[name])
        data += get_table(EXT + urls[name], name)
        time.sleep(1)
    # write all contents
    fp.write(data)
    fp.close()

    return

def create_CSV(urls):
    # get permission to write
    fp = open("data/stats.csv", 'w+')
    # obtain data
    data = ""
    for name in urls:
        print(name + " " + EXT+urls[name])
        data += get_table(EXT + urls[name], name)
        time.sleep(1)
    # write all contents
    fp.write(data)
    fp.close()

    return

# get comma delimited text of per_game data of ~500 players in league
def get_table(player_url, name):
    url = player_url
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    # find the table rows
    rows = soup.find('table', attrs={'id': table }).find('tbody').find_all('tr')
    buffer = ""
    # traverse per_game data for relevent years
    for row in rows:
        # check for missing values
        tds = row.find_all('td')
        indices = []
        i = 0
        for td in tds:
            if (td.get_text() == ""):
                indices.append(i)
            i += 1
        # reverse the HTML element indices to ease substring replacements
        indices = indices[::-1]
        # get data in row
        temp = row.get_text(",") + "\n"
        if year in temp:
            # correct stat line if needed
            for j in indices:
                k = 0
                identifier = ""
                while (k < j):
                    # get text of next <td></td>
                    str = tds[k].get_text()
                    # check for data to avoid a non-existent comma
                    if (str != ""):
                        identifier += str + ","
                    k += 1
                # replace with corrected stat line
                temp = temp.replace(identifier, identifier+"0,")

            # add stat line to matrix
            buffer += "\"" + name + "\"," + temp
            # this break only keeps the total stats for traded players
            break

    return buffer

## end
