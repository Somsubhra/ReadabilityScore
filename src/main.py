from Runner import *
from os import path


def main():
    print "Starting the program..."
    r = Runner(path.join('corpus', 'training'), path.join('corpus', 'testing'), 'out')
    r.run()
    print "Program ended..."

if __name__ == '__main__':
    main()