# import libraries
#import time
import sys
import os
import json
from player_stats import create_CSV
#import player_urls.py

#from datetime import datetime

def main (argv):
    # argv format: teams, players, (options) years
    if (len(argv) == 1):
        print("USAGE> python scraper.py ['all' | 'John,Wall Bradley,Beal' | 'urls']")
        quit()

    if (argv[1] == "all"):
        # have function to call module for all players
        dirtyURLs = []
        with open('data/urls.json') as jsonData:
            dirtyURLs = json.load(jsonData)
            urls = dirtyURLs["players"]
            #print (dirtyURLs)

        #urls = dirtyURLs["Tony Snell"]
        #print(urls)
        # create the array of links
        data = create_CSV(urls)
    else:
        for term in argv:
            # make call to module
            print (term)

    # return data
    return 1


if __name__ == "__main__":
    main(sys.argv)

## end
