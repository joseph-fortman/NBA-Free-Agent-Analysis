import pandas as pd
import matplotlib.pyplot as plt

training_file = 'data/matrix.csv'

def display_stats(w_hat, y):
    df = pd.read_csv(training_file)
    #Xdf = pd.DataFrame(X, index=names, columns=labels)
    print(df)

    r,c = X.shape

    fig, ax = plt.subplots()
    for i in range(0,r):
        ax.plot(labels, X[i,:], label=names[i])
    ax.legend()
    plt.show()

    return
