import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import model.display as disp


def calc (X,y):
    # calculate eigenvectors and eignevalues
    [U,S,V] = np.linalg.svd(X, full_matrices=False)
    V = V.T

    # Print for analysis
    disp.eigenvalues(S)
    disp.eigenvectors(U,V)

    # least squares approximation using eigenvectors and eignevalues
    w_hat = V @ np.linalg.inv(np.diag(S)) @ U.T @ y

    return w_hat

def cross_validate (X,y):
    a,b = X.shape

    sets = 10
    group_size = a / sets

    # cross validate model
    avg_accuracy = 0;

    for j in range(sets):
        # get dataset splits
        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.2)
        # least squares minimization
        w_hat = calc(X_train, y_train)
        y_hat = X_test * w_hat
        total_correct = total_correct + check(y_hat,y_test);

    avg_accuracy = total_correct/sets;

    return avg_accuracy
