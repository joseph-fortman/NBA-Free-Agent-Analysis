import numpy as np
import pandas as pd

weights_file = 'data/weights.csv'

def classify(argv):
    # check argv[2]
    if (argv[2] == '-h') or (argv[2] == '--help'):
        print("python app.py classify 'data/<new k filename>'")

    classify_file = argv[2]
    print (classify_file)

    # handle errors here
    X = np.genfromtxt(classify_file, delimiter=',')
    # if X.shape will cause an error (one new k being tested)
    # take out the name... Might be easier to use pandas again...

    # load and reshape predicted w vector
    a,b = X.shape # having only one player tested causes an error
    w_hat = np.genfromtxt(weights_file, delimiter=',')
    w_hat = np.reshape(w_hat, (b,1))
    # calculate classification
    y_hat = X @ w_hat

    print(y_hat)

    # here I need a good way to visualize the predictions
