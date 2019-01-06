'''
compile.py is used to perform data cleaning after scraping is complete. Such code
becomes relatively messy. These modules handle such mess and provide flexibility
as data sources change over time.

compile.py compiles all data into one matrix which is placed into matrix.csv.
Then, matrix X and result vector y used in least squares computations can be
read during the modeling stage without any issues or excessive code.
'''

def compile(argv):
    # check argv[2]
    if (argv[2] == '-h' || argv[2] == '--help'):
        print("Make sure that all of the required data is in the following files:\n\
            data/stats\
            data/salaries\
            data/analysis")

    # start loading the data into X
