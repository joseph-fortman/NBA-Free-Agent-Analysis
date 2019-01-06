import sys
from modules.classifier import create_classifier
from modules.classifier import display

import pandas as pd
import numpy as np

def main (argv):
    # argv format: teams, players, (options) years
    if (len(argv) == 1):
        print("USAGE> python model.py ['<training filename>']")
        quit()

    # new classifier
    if (argv[1] == 'new'):
        train_filename = argv[2]
        w_hat = create_classifier(train_filename)
        print(w_hat.tostring)
        quit()
        # write least squares weights
        fp = open("data/weights.csv", 'w')
        fp.write(w_hat.tostring())
        fp.close()

    elif (argv[1] == 'test'):
        X = np.genfromtxt('data/test-matrix.csv', delimiter=',')
        names_pos = np.genfromtxt('data/test-matrix.csv', dtype=('|S20'), delimiter=',', usecols=[0,5])
        names = names_pos[:,0]
        positions = names_pos[:,1]
        # data clean up
        cols = [5,4,3,1,0]
        for col in cols:
            X = np.delete(X, col, 1)

        display(X, names)


    # success
    return 1


if __name__ == "__main__":
    main(sys.argv)

## end
