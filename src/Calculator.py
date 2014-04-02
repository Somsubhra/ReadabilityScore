from math import sqrt
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

    # Calculate smog index
    def smog_index(self):
        return 1.0430 * sqrt(float(self.parser.number_of_polysyllables()) * 30.0 / float(self.parser.number_of_sentences()))\
               + 3.1291

    # Calculate flesch reading ease
    def flesch_reading_ease(self):
        return 206.835 - 1.105 * (float(self.parser.number_of_words()) / float(self.parser.number_of_sentences())) - \
               84.6 * (float(self.parser.number_of_syllables()) / float(self.parser.number_of_words()))

    # Calculate Flesch Kincaid grade level
    def flesch_kincaid_grade_level(self):
        return (0.39 * float(self.parser.average_sentence_length())) + (11.8 * self.parser.average_syllable_per_word()) \
               - 15.59

    # Calculate Coleman Liau index
    def coleman_liau_index(self):
        return 0.0588 * (float(self.parser.average_letter_per_100_words())) \
               - 0.296 * (self.parser.average_sentences_per_100_words()) - 15.8