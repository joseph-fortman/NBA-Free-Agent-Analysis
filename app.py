import sys
from scrape.scrape import scrape
from compile.compile import compile
from model.model import model
from classify.classify import classify

def main (argv):
    # argv format
    if (len(argv) == 1):
        print("USAGE> python app.py ['scrape' | 'compile' | 'model' | 'classify']")
        return -1

    # direct app
    if (argv[1] = 'scrape'):
        scrape(argv)
    elif (argv[1] = 'compile'):
        compile(argv)
    elif (argv[1] = 'model'):
        model(argv)
    elif (argv[1] = 'classify'):
        classify(argv)
    else:
        print("USAGE> python app.py ['scrape' | 'compile' | 'model' | 'classify']")
        return -1

    # success
    return 1


if __name__ == "__main__":
    main(sys.argv)

## end
