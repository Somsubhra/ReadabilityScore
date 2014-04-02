from Runner import *
from os import path


def main():
    r = Runner(path.join('corpus', 'training'), path.join('out', 'training'))
    r.run()

if __name__ == '__main__':
    main()