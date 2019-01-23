import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import model.display as disp
from sklearn.model_selection import train_test_split


# test various models
def cross_validate (X,y):
    a,b = X.shape

    # cross validate model
    total_ac = 0
    sets = 10
    best = 0
    weights = []
    X_final = []
    lambdas = [.001, .01, .1, 1, 5, 10, 100, 1000, 10000, 100000]

    for j in range(sets):
        # get dataset splits
        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.2)
        # least squares minimization
        w_hat = calc(X_train, y_train)
        #w_hat = Tikhonov (X_train, y_train, lambdas[j])
        y_hat = X_test @ w_hat
        # get correct predition percentage
        accuracy = check(y_hat,y_test)

        # save best results
        if (accuracy > best):
            best = accuracy
            weights = w_hat
            X_final = X_train
        # sum for analysis
        total_ac = total_ac + accuracy

    # display kept Eigenvalues/vectors and weights
    disp.eigens(X_final)

    # avgerage accuracy
    print ("Average Accuracy")
    print (total_ac/sets)
    print ("Best Accuracy")
    print (best)
    # return final weights and average accuracy
    return weights


# calculate a classifier
def calc (X,y):
    # calculate eigenvectors and eignevalues
    [U,S,V] = np.linalg.svd(X, full_matrices=False)
    # least squares approximation using eigenvectors and eignevalues
    w_hat = V.T @ np.linalg.inv(np.diag(S)) @ U.T @ y

    return w_hat

# calculate a Tikhonov Regression classifier
def Tikhonov (X,y,l):
    #disp.eigens(X)
    # calculate eigenvectors and eignevalues
    [U,S,V] = np.linalg.svd(X, full_matrices=False)
    # simplify equation
    S = np.diag(S)
    a,b = S.shape
    I = np.identity(a)
    S2 = np.square(S)
    # Tikhonov regularized least squares approximation using SVD
    w_hat = V.T @ np.linalg.inv(S2 + l*I) @ U.T @ y

    return w_hat

# count correct predictions
def check(y_hat, y):
    # round values
    y_hat[(y_hat < -2.5)] = -3
    y_hat[(y_hat > -2.5) & (y_hat < -1.5)] = -2
    y_hat[(y_hat > -1.5) & (y_hat < -0.5)] = -1
    y_hat[(y_hat > -0.5) & (y_hat < 0.5)] = 0
    y_hat[(y_hat > 0.5) & (y_hat < 1.5)] = 1
    y_hat[(y_hat > 1.5) & (y_hat < 2.5)] = 2
    y_hat[(y_hat > 2.5)] = 3

    #print (y_hat)
    #print (y)
    #print ("-")

    z = y_hat - y
    incorrect = np.count_nonzero(z)
    correct = len(y) - incorrect
    return correct / len(y)
