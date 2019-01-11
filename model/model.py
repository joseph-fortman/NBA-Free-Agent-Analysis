import numpy as np
from model.least_squares import calc
import model.display

training_file = 'data/matrix.csv'
result_file = 'data/result.csv'
weights_file = 'data/weights.csv'

# create new classifier
def model (argv):

    # load training matrix
    print(training_file)
    X = np.genfromtxt('data/matrix.csv', delimiter=',', skip_header=1)
    # handle random nan values
    np.nan_to_num(X, copy=False)

    # load subjective results vector and reshape to avoid (x,)
    a,b = X.shape
    y = np.genfromtxt(result_file, usecols=0)
    y = np.reshape(y,(a,1))

    w_hat = calc(X,y)

    print(w_hat.tostring)
    # write least squares weights
    fp = open(weights_file, 'w')
    fp.write(w_hat.tostring()) # doesn't work
    fp.close()

    names = np.genfromtxt(training_file, dtype=('|S20'), delimiter=',', usecols=[0])

    display.display_stats(X, names)

    # success
    return 1

## end
