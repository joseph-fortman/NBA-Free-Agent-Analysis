'''

'''

import numpy as np
import pandas as pd

def classify(argv):
    # check argv[2]
    if (argv[2] == '-h' || argv[2] == '--help'):
        print("python classify.py ['<new k filename>']")

    filename = argv[2]
    print (filename)

    # handle errors here
    X = np.genfromtxt(filename, delimiter=',')
    w_hat = np.genfromtxt('data/weights.csv', delimiter=',')
    # do I need to import numpy for this?
    y_hat = X @ w_hat
    print (y_hat)
    # here I need a good way to visualize the predictions
