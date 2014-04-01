from Calculator import *
from os import walk, path, stat, mkdir


# The Runner class
class Runner:

    # Constructor for the runner class
    def __init__(self, input_directory, output_directory):
        self.input_directory = input_directory
        self.output_directory = output_directory

    # The main running method for the runner
    def run(self):

        # Create output directory
        try:
            stat(self.output_directory)
        except:
            mkdir(self.output_directory)

        # Write to output file
        output_file = open('out/result.csv', 'w+')

        output_file.write("\"Filename\";\"Number of words\";\"Number of sentences\";"
                          "\"Avg. words per sentence\";\"Avg. word length\";\"Number of Jukthakshars\""
                          ";\"Avg. syllable per word\";\"Number of polysyllables\";\""
                          "Number of Polysyllables per 30 sentences\"\n")

        # Walk through all files in tree
        for (dir_path, _, file_names) in walk(self.input_directory):
            for filename in file_names:
                test_file = path.join(dir_path, filename)

                # The index calculator
                c = Calculator(test_file)

                # The parser
                p = c.parser

                print c.gunning_fog_index()

                # The output line
                output_line = "\"" + str(test_file) + "\";\"" + str(p.number_of_words()) + "\";\"" +\
                              str(p.number_of_sentences()) + "\";\"" + str(p.average_words_per_sentence()) \
                              + "\";\"" + str(p.average_word_length()) + "\";\"" + str(p.number_of_jukthakshar()) +\
                              "\";\"" + str(p.average_syllable_per_word()) + "\";\"" + str(p.number_of_polysyllables())\
                              + "\";\"" + str(p.number_of_polysyllables_per_30_sentences()) + "\"\n"

                output_file.write(output_line)

        output_file.close()