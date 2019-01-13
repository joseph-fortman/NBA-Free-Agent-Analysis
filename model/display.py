import pandas as pd
import matplotlib.pyplot as plt

training_file = 'data/matrix.csv'
names_file = 'data/names.csv'

def display_stats(w_hat, y):
    names = pd.read_csv(names_file, names=['Name'])
    df = pd.read_csv(training_file)

    r,c = df.shape

    fig, ax = plt.subplots()
    for i in range(0,15):
        ax.plot(list(df), df.iloc[i,:], label=names.iloc[i,0])
    ax.legend()
    plt.show()

    return
