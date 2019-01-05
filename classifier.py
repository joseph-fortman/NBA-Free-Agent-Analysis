import numpy as np
import matplotlib.pyplot as mpl

def attempt_display():
    labels = ["Age", "G", "GS", "MP", "FG", "FGA", "FG%", "3P", "3PA", "3P%", "2P", "2PA", "2P%", "eFG%", "FT", "FTA", "FT%", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS"]
    # load training matrix
    X = np.genfromtxt("test-matrix.csv", delimiter=',')
    # data clean up
    cols = [5,4,3,1,0]
    for col in cols:
        X = np.delete(X, col, 1)

    fig, ax = mpl.subplots()
    ax.plot(labels, X[0,:], label="player1")
    ax.plot(labels, X[1,:], label="player2")
    ax.plot(labels, X[2,:], label="player3")
    ax.plot(labels, X[3,:], label="player4")
    ax.legend()
    mpl.show()

    return

def create_classifier(train_filename):
    # load training matrix
    X = np.genfromtxt(train_filename, delimiter=',')
    # mitigate damage of missing data
    np.nan_to_num(X, copy=False)
    # data clean up
    cols = [5,4,3,1,0]
    for col in cols:
        X = np.delete(X, col, 1)

    print(X.shape)
    quit()

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
