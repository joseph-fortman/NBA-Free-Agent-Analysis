import sys
from classifier import create_classifier

def main (argv):
    # argv format: teams, players, (options) years
    if (len(argv) == 1):
        print("USAGE> python free_agent_analysis.py ['<filename>' | 'classifier']")
        quit()

    if (argv[1] == 'classifier'):
        create_classifier()

    else:
        print(argv[1])
        # check for the file and catch exceptions

    # success
    return 1


if __name__ == "__main__":
    main(sys.argv)

## end
