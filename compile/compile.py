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

convert = {'PG':1, 'PG-SG':1, 'SG-PG':2, 'SG':2, 'SG-SF':2, 'SF-SG':3, 'SF':3, 'SF-PF':3, 'PF-SF':4, 'PF':4, 'PF-C':4, 'C-PF':5, 'C':5, 'SG-PF':2}
labels = ["Age", "G", "GS", "MP", "FG", "FGA", "FG%", "3P", "3PA", "3P%", "2P", "2PA", "2P%", "eFG%", "FT", "FTA", "FT%", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS"]

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
    positions = pd.read_csv(stats_loc, names=["Pos"], usecols=[5], dtype=str)
    positions = positions.replace({"Pos":convert})

    # concatenate positions and stats
    df = pd.DataFrame(X, columns=labels)
    df = pd.concat([positions,df], axis=1)

    r,c = df.shape
    print("\n--Updated--\nmatrix.csv\n({},{})".format(r,c))

    df.to_csv(matrix_loc, index=False)

##end
