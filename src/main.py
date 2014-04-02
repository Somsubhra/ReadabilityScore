from Runner import *
from os import path


def main():
    r = Runner(path.join('corpus', 'training'), path.join('out', 'training'),
               path.join('corpus', 'testing'), path.join('out', 'testing'))
    r.run()

if __name__ == '__main__':
    main()