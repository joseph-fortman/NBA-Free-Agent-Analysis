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

# generate model
def cross_validate (X,y):
    a,b = X.shape

    # cross validate model
    total_correct = 0
    sets = 10

    for j in range(sets):
        # get dataset splits
        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.2)
        # least squares minimization
        w_hat = calc(X_train, y_train)
        y_hat = X_test * w_hat
        # get correct predition percentage
        correct = check(y_hat,y_test)
        # save best results
        if (correct > best):
            best = correct
            weights = w_hat
        # sum for analysis
        total_correct = total_correct + correct

    # display kept Eigenvalues/vectors and weights

    avg_accuracy = total_correct/sets;
    # return final weights and average accuracy
    return (weights, avg_accuracy)

# count correct predictions
def check(y_hat, y):
    z = y_hat - y
    incorrect = np.count_nonzero(z)
    correct = len(y) - incorrect
    return correct
