from Runner import *
from os import path


def main():
    r = Runner(path.join('corpus', 'training'), path.join('corpus', 'testing'), 'out')
    r.run()

if __name__ == '__main__':
    main()