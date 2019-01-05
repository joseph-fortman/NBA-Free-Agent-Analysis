import sys
from classifier import create_classifier
from classifier import attempt_display

def main (argv):
    # argv format: teams, players, (options) years
    if (len(argv) == 1):
        print("USAGE> python free_agent_analysis.py ['run <new k filename>' | 'new <training filename>']")
        quit()

    # new classifier
    if (argv[1] == 'new'):
        train_filename = argv[2]
        w_hat = create_classifier(train_filename)
        # write least squares weights
        fp = open("data/weights.csv", 'w+')
        fp.write(w_hat)
        fp.close()

    elif (argv[1] == 'run'):
        filename = argv[2]
        # handle errors here
        X = np.genfromtxt(filename, delimiter=',')
        w_hat = np.genfromtxt('data/weights.csv', delimiter=',')
        # do I need to import numpy for this?
        y_hat = X @ w_hat

        # here I need a good way to visualize the predictions
    else:
        attempt_display()


    # success
    return 1


if __name__ == "__main__":
    main(sys.argv)

## end
