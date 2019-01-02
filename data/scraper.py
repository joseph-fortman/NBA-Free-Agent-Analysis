# import libraries
#import time
import sys
import os
#import player_stats.py
#import player_urls.py

#from datetime import datetime

# placeholder, might be effective though
def create_CSV(data):
    # write all contents
    fp = open("stats.csv", 'w+')
    fp.write(data)
    fp.close()

def main (argv):
    # argv format: teams, players, (options) years
    if (len(argv) == 0):
        quit()

    if (argv[1] == "all"):
        # have function to call module for all players
        print (all)
    else:
        for term in argv:
            # make call to module
            print (term)

    # return data
    return 1


if __name__ == "__main__":
    main(sys.argv)

## end
