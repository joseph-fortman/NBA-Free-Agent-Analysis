import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def display(X, names):
    labels = ["Age", "G", "GS", "MP", "FG", "FGA", "FG%", "3P", "3PA", "3P%", "2P", "2PA", "2P%", "eFG%", "FT", "FTA", "FT%", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS"]
    Xdf = pd.DataFrame(X, index=names, columns=labels)
    print(Xdf)

    r,c = X.shape

    fig, ax = plt.subplots()
    for i in range(0,r):
        ax.plot(labels, X[i,:], label=names[i])
    ax.legend()
    plt.show()

    return
