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
    X = np.genfromtxt(training_file, delimiter=',', skip_header=1)
    # handle random nan values. IS THIS NEEDED? I'm guessing no
    np.nan_to_num(X, copy=False)

    # load subjective results vector and reshape to avoid (x,)
    a,b = X.shape
    y = np.genfromtxt(result_file, usecols=0)
    y = np.reshape(y,(a,1))
    # calculate least squares regression
    w_hat = calc(X,y)

    # write least squares weights
    np.savetxt(weights_file, w_hat, delimiter=',')

    display.display_stats(w_hat, y)

    # success
    return 1

## end
