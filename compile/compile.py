'''
compile.py is used to perform data cleaning after scraping is complete. Such code
becomes relatively messy. These modules handle such mess and provide flexibility
as data sources change over time.

compile.py compiles all data into one matrix which is placed into matrix.csv.
Then, matrix X and result vector y used in least squares computations can be
read during the modeling stage without any issues or excessive code.
'''

import numpy as np
import pandas as pd

stats_loc = 'data/stats.csv'
salaries_loc = 'data/salaries.csv'
matrix_loc = 'data/matrix.csv'

convert = {'PG':1, 'SG':2, 'SF':3, 'PF':4, 'C':5, 'C-':5}

def compile(argv):
    # check argv[2]
    if (len(argv) == 3):
        if (argv[2] == '-h') or (argv[2] == '--help'):
            print("Make sure that all of the required data is in the following files:\n\
                - data/stats\
                - data/salaries")

    # start loading the data into X
    X = np.genfromtxt(stats_loc, delimiter=',')
    # clean data
    cols = [5,4,3,1,0]
    for col in cols:
        X = np.delete(X, col, 1)
    # convert PG,SG,SF,PF,C -> 1,2,3,4,5
    names = np.genfromtxt(stats_loc, dtype=('|S20'), delimiter=',', usecols=[0])
    positions = np.genfromtxt(stats_loc, dtype=('|S20'), delimiter=',', usecols=[5])
    X = [positions,X]
    print(X)
    labels = ["Pos", "Age", "G", "GS", "MP", "FG", "FGA", "FG%", "3P", "3PA", "3P%", "2P", "2PA", "2P%", "eFG%", "FT", "FTA", "FT%", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS"]
    df = pd.DataFrame(X, index=names, columns=labels)

    print(df)
    #df[1].apply(map(lambda x: ))

    #[positions,stats]

def numeric_positions(v):
    v[i][:2]
