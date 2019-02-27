import os
import json
from scrape.player_stats import create_CSV
from scrape.player_urls import update_URLs

year = "2019"
group_file = "data/group.csv"
full_file = "data/stats.csv"

def scrape (argv):
    # argv format: teams, players, (options) years
    if (len(argv) == 1):
        print("USAGE> python app.py scrape ['all' | 'John,Wall Bradley,Beal' | 'urls']")
        quit()

    # get all players' per_game stats
    if (argv[2] == "all"):
        with open('data/urls.json') as jsonData:
            urls = json.load(jsonData)
        # send dict of (name : relative url) pairs
        create_CSV(urls, full_file)

    # update abc.json with relative player page links
    elif (argv[2] == "urls"):
        update_URLs(year)

    # treat other arguments as single player names (handle issues)
    else:
        with open('data/urls.json') as jsonData:
            urls = json.load(jsonData)
        group = {}
        for term in argv:
            if ("app.py" in term) or ("scrape" in term):
                continue
            # correct name
            term = term.replace(",", ", ")
            group[term] = urls[term]

        # make call to module
        create_CSV(group, group_file)


    # success
    return 1

## end
