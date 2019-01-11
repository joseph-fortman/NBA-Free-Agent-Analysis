import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def calc(X,y):

    r,c = X.shape

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
