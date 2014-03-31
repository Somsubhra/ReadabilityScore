from Parser import *


def main():
    p = Parser('res/test')
    print p.number_of_words()
    print p.words
    print p.number_of_sentences()
    print p.average_words_per_sentence()
    print p.average_word_length()
    print p.number_of_jukthakshar()

if __name__ == '__main__':
    main()