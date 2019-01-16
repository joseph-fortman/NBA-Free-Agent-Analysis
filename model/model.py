import numpy as np
from model.least_squares import calc
import model.display as disp

training_file = 'data/matrix.csv'
result_file = 'data/result.csv'
weights_file = 'data/weights.csv'

# create new classifier
def model (argv):
    # load training matrix
    X = np.genfromtxt(training_file, delimiter=',', skip_header=1)
    disp.pay_trends(X)
    # load subjective results vector and reshape to avoid (x,)
    a,b = X.shape
    y = np.genfromtxt(result_file, usecols=0)
    y = np.reshape(y,(a,1))
    # calculate least squares regression
    w_hat = calc(X,y)

    # write least squares weights
    np.savetxt(weights_file, w_hat, delimiter=',')

    disp.stats(w_hat, y)

    # success
    return 1

## end
