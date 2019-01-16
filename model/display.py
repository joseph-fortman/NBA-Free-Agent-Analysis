import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

training_file = 'data/matrix.csv'
names_file = 'data/names.csv'

def stats(w_hat, y):
    names = pd.read_csv(names_file, names=['Name'])
    df = pd.read_csv(training_file)

    r,c = df.shape

    fig, ax = plt.subplots()
    for i in range(0,15):
        ax.plot(list(df), df.iloc[i,:], label=names.iloc[i,0])
    ax.legend()
    plt.show()

    return

# display eigenvalues for analysis
def eigenvalues(Sigma):
    # plot and save model Eigenvalues
    fig, ax = plt.subplots()
    index = np.arange(len(Sigma))

    ax.plot(index, Sigma, 'go')
    ax.set(xlabel='index', ylabel='S value', title='Eigenvalues')
    ax.grid()

    fig.savefig("model/test.png")
    plt.show()

    # print dimensions
    print ("S:")
    print (Sigma.shape)
    return

def eigenvectors(U,V):
    print("U: ")
    print(U.shape)
    print("V: ")
    print(V.shape)
    return
