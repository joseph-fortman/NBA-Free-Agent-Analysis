import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import model.display as disp


def calc(X,y):

    r,c = X.shape

    # calculate eigenvectors and eignevalues
    [U,S,V] = np.linalg.svd(X, full_matrices=False)
    V = V.T

    disp.eigenvalues(S)
    disp.eigenvectors(U,V)

    # least squares approximation using eigenvectors and eignevalues
    w_hat = V @ np.linalg.inv(np.diag(S)) @ U.T @ y

    return w_hat
