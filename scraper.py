import sys
import os
import json
from player_stats import create_CSV
from player_stats import group_CSV
from player_urls import update_URLs

def main (argv):
    # argv format: teams, players, (options) years
    if (len(argv) == 1):
        print("USAGE> python scraper.py ['all' | 'John,Wall Bradley,Beal' | 'urls']")
        quit()

    # get all players' per_game stats
    if (argv[1] == "all"):
        with open('data/urls.json') as jsonData:
            urls = json.load(jsonData)
        # send dict of (name : relative url) pairs
        create_CSV(urls)

    # update abc.json with relative player page links
    elif (argv[1] == "urls"):
        year = "2019"
        update_URLs(year)

    # treat other arguments as single player names (handle issues)
    else:
        with open('data/urls.json') as jsonData:
            urls = json.load(jsonData)
        group = {}
        for term in argv:
            if ("scraper.py" in term):
                continue
            # correct name
            term = term.replace(",", " ")
            group[term] = urls[term]

        # make call to module
        group_CSV(group)


    # success
    return 1


if __name__ == "__main__":
    main(sys.argv)

## end
