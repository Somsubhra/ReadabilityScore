from Parser import *


def main():
    p = Parser('res/test')
    print p.number_of_words()
    print p.words
    print p.number_of_sentences()

if __name__ == '__main__':
    main()