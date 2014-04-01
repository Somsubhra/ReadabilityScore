from Parser import *


# The index calculator class
class Calculator:

    # Constructor for the Calculator class
    def __init__(self, filename):
        self.parser = Parser(filename)

    # Calculate Automatic Readability Index
    def automated_readability_index(self):
        return 4.71 * (float(self.parser.number_of_characters()) / float(self.parser.number_of_words())) \
               + 0.5 * (float(self.parser.number_of_words()) / float(self.parser.number_of_sentences())) - 21.43

    # Calculate Gunning fog index
    def gunning_fog_index(self):
        return 0.4 * ((float(self.parser.number_of_words()) / float(self.parser.number_of_sentences()))
                      + 100 * (float(self.parser.number_of_polysyllables()) / float(self.parser.number_of_words())))