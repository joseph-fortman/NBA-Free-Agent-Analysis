import numpy as np
from model.least_squares import calc
import model.display

training_file = '../data/matrix.csv'
weights_file = '../data/weights.csv'

# create new classifier
def model (argv):

    # load training matrix
    X = np.genfromtxt(train_file, delimiter=',')
    # handle file not found errors
    # load subjective results vector
    y = np.ones((r,1))

    w_hat = calc(X,y)
    print(w_hat.tostring)

    # write least squares weights
    fp = open(weights_file, 'w')
    fp.write(w_hat.tostring()) # doesn't work
    fp.close()

    names = np.genfromtxt(train_file, dtype=('|S20'), delimiter=',', usecols=[0])

    display.display_stats(X, names)

    # success
    return 1

## end
