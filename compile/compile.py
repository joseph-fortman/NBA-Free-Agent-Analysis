import pandas as pd
import matplotlib.pyplot as plt

stats_loc = 'data/stats.csv'
salaries_loc = 'data/salaries.csv'
matrix_loc = 'data/matrix.csv'
names_loc = 'data/names.csv'

convert = {'PG':1, 'PG-SG':1, 'SG-PG':2, 'SG':2, 'SG-SF':2, 'SF-SG':3, 'SF':3, 'SF-PF':3, 'PF-SF':4, 'PF':4, 'PF-C':4, 'C-PF':5, 'C':5, 'SG-PF':2}
labels = ["Name", "Age", "Pos", "G", "GS", "MP", "FG", "FGA", "FG%", "3P", "3PA", "3P%", "2P", "2PA", "2P%", "eFG%", "FT", "FTA", "FT%", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS"]

# start main

def compile(argv):
    # check argv[2]
    if (len(argv) == 3):
        if (argv[2] == '-h') or (argv[2] == '--help'):
            print("Make sure that all of the required data is in the following files:\n\
                - data/stats\
                - data/salaries")

    # read scraped data
    salary_df = salaries()
    stats_df = stats()
    # only keep intersection of DataFrames
    df = stats_df.merge(salary_df, how='inner', on='Name')
    names = df['Name']
    # name column not needed anymore
    df.drop(labels='Name', axis=1, inplace=True)
    TEMP_DISPLAY(df)
    # write cleansed data
    df.to_csv(matrix_loc, index=False)
    names.to_csv(names_loc, index=False)

    r,c = df.shape
    print("\n--Updated--\nmatrix.csv\n({},{})".format(r,c))

    return 1

# end main
# start functions

def salaries():
    # read
    df = pd.read_csv(salaries_loc)
    # fill NaN (years after current k ends) with 0
    df = df.fillna(0)
    # create list of column headers and remove last three
    col_list = list(df)
    detail_cols = ['Name','NG years','PO years','TO years']
    for col in detail_cols:
        col_list.remove(col)

    # count rows without zeros
    df['years left'] = (df[col_list] != 0).astype(int).sum(axis=1)
    # sum player rows 0-5
    df['salary left'] = df[col_list].sum(axis=1)
    # drop yearly payment columns
    df.drop(df.columns[[1, 2, 3, 4, 5, 6]], axis=1, inplace=True)

    return df

def stats():
    # clean data -- remove year, team, "NBA" columns
    list = [4,3,1]
    cols = [i for i in range(31)]
    for i in list:
        del cols[i]
    # read csv
    df = pd.read_csv(stats_loc, names=labels, usecols=cols)
    # convert PG,SG,SF,PF,C -> 1,2,3,4,5
    return df.replace({"Pos":convert})

def TEMP_DISPLAY(df):
    # What do GMs pay the most for?
    df['per year'] = df['salary left'] / df['years left']
    #print(df['per year'])
    df = df.sort_values(by=['per year'])
    df.drop(df.columns[[27,28,29,30,31]], axis=1, inplace=True)
    arr = df.values
    print(arr)
    print(arr.dtype)

    fig, ax = plt.subplots()
    ax.pcolormesh(arr)

    plt.show()

    quit()

# end functions
