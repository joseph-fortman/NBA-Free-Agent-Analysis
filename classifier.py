import numpy as np

def create_classifier():
    # load matrix
    X = np.genfromtxt('test-matrix.csv', delimiter=',')
    # data clean up
    cols = [5,4,3,1,0]
    for col in cols:
        X = np.delete(X, col, 1)
    # mitigate damage of missing data
    np.nan_to_num(X, copy=False)

    # load subjective results vector
    y = np.ones((4,1))
    y[2] = 0
    print(y)

    # calculate eigenvectors and eignevalues
    [U,S,VH] = np.linalg.svd(X, full_matrices=False)
    V = VH.T

    #print(U)
    #print(np.diag(S))
    #print(V)
    # least squares approximation using eigenvectors and eignevalues
    w_hat = V @ np.linalg.inv(np.diag(S)) @ U.T @ y
    print(w_hat)

    return w_hat
