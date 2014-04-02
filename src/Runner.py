from Calculator import *
from Generator import *
from os import walk, path, stat, mkdir


# The Runner class
class Runner:

    # Constructor for the runner class
    def __init__(self, input_train_directory, input_test_directory, output_directory):
        self.input_train_directory = input_train_directory
        self.output_directory = output_directory
        self.input_test_directory = input_test_directory

    # The main running method for the runner
    def run(self):

        print "Started the program..."

        # Start the training
        print "Started training from the training data..."

        asl = []
        awl = []
        asw = []
        psw30 = []
        juk30 = []

        difficulty = {}
        difficulty_scores = []

        lines = open('manual_difficulty_scores').readlines()

        print "Reading the manual difficulty levels given to training data..."

        for line in lines:
            if line == '\n':
                break
            line = str(line).split(':')
            difficulty[line[0]] = int(line[1])

        # Create output directory
        try:
            stat(self.output_directory)
        except:
            mkdir(self.output_directory)

        print "Writing stats of training data to " + self.output_directory + "\stats_training.csv..."

        # Write to output file
        output_file = open(path.join(self.output_directory, 'stats_training.csv'), 'w+')
        output_file.write("\"Filename\";\"ASL\";\"AWL\";\"ASW\";\"PSW30\";\"JUK30\"\n")

        print "Calculating English Readability indices for training data..."
        print "Added them to " + self.output_directory + "\english_index_training.csv..."

        english_index_file = open(path.join(self.output_directory, 'english_index_training.csv'), 'w+')
        english_index_file.write("\"Filename\";"
                                 "\"Automatic Readability Index\";"
                                 "\"Gunning Fog Index\";"
                                 "\"Smog Index\";"
                                 "\"Flesch Reading Ease\";"
                                 "\"Flesch Kincaid Grade Level\";"
                                 "\"Coleman Liau Index\"\n")

        # Walk through all files in tree
        for (dir_path, _, file_names) in walk(self.input_train_directory):
            for filename in file_names:
                test_file = path.join(dir_path, filename)

                # The index calculator
                c = Calculator(test_file)

                # The parser
                p = c.parser

                if difficulty.has_key(test_file):
                    difficulty_scores.append(difficulty[test_file])
                    asl.append(p.average_sentence_length())
                    awl.append(p.average_word_length())
                    asw.append(p.average_syllable_per_word())
                    psw30.append(p.number_of_polysyllables_per_30_sentences())
                    juk30.append(p.number_of_jukthakshar_per_30_words())

                # The output line
                output_line = "\"" + str(test_file) \
                              + "\";\"" \
                              + str(p.average_sentence_length())\
                              + "\";\"" \
                              + str(p.average_word_length())\
                              + "\";\"" \
                              + str(p.average_syllable_per_word()) \
                              + "\";\"" \
                              + str(p.number_of_polysyllables_per_30_sentences()) \
                              + "\";\""\
                              + str(p.number_of_jukthakshar_per_30_words())\
                              + "\"\n"

                output_file.write(output_line)

                english_index_output_line = "\"" + str(test_file) \
                                            + "\";\"" \
                                            + str(c.automated_readability_index())\
                                            + "\";\"" \
                                            + str(c.gunning_fog_index())\
                                            + "\";\"" \
                                            + str(c.smog_index()) \
                                            + "\";\""\
                                            + str(c.flesch_reading_ease()) \
                                            + "\";\"" \
                                            + str(c.flesch_kincaid_grade_level()) \
                                            + "\";\""\
                                            + str(c.coleman_liau_index())\
                                            + "\"\n"

                english_index_file.write(english_index_output_line)

        output_file.close()
        english_index_file.close()

        # Generate the index
        print "Generating the custom index using Correlation and Linear Regression..."

        g = Generator(asl, awl, asw, psw30, juk30, difficulty_scores, self.output_directory)
        g.generate()

        # Stop the training

        # Start testing

        # Write to output file

        print "Start testing on testing data..."

        print "Calculating stats for testing data..."
        print "Writing stats to " + self.output_directory + "\stats_testing.csv..."

        output_file = open(path.join(self.output_directory, 'stats_testing.csv'), 'w+')
        output_file.write("\"Filename\";\"ASL\";\"AWL\";\"ASW\";\"PSW30\";\"JUK30\"\n")

        print "Calculating English Indices on testing data..."
        print "Applying our custom formula to testing data..."
        print "Output written to " + self.output_directory + "\index_testing.csv..."

        index_file = open(path.join(self.output_directory, 'index_testing.csv'), 'w+')
        index_file.write("\"Filename\";"
                         "\"Generated Index Value\";"
                         "\"Automatic Readability Index\";"
                         "\"Gunning Fog Index\";"
                         "\"Smog Index\";"
                         "\"Flesch Reading Ease\";"
                         "\"Flesch Kincaid Grade Level\";"
                         "\"Coleman Liau Index\"\n")

        # Walk through all files in tree
        for (dir_path, _, file_names) in walk(self.input_test_directory):
            for filename in file_names:
                test_file = path.join(dir_path, filename)

                # The index calculator
                c = Calculator(test_file)

                index = g.custom_index(test_file)

                # The parser
                p = c.parser

                # The output line
                output_line = "\"" + str(test_file) \
                              + "\";\"" \
                              + str(p.average_sentence_length())\
                              + "\";\"" \
                              + str(p.average_word_length())\
                              + "\";\"" \
                              + str(p.average_syllable_per_word()) \
                              + "\";\"" \
                              + str(p.number_of_polysyllables_per_30_sentences()) \
                              + "\";\""\
                              + str(p.number_of_jukthakshar_per_30_words())\
                              + "\"\n"

                output_file.write(output_line)

                index_output_line = "\"" \
                                    + str(test_file) \
                                    + "\";\"" \
                                    + str(index) \
                                    + "\";\"" \
                                    + str(c.automated_readability_index())\
                                    + "\";\"" \
                                    + str(c.gunning_fog_index())\
                                    + "\";\"" \
                                    + str(c.smog_index()) \
                                    + "\";\""\
                                    + str(c.flesch_reading_ease()) \
                                    + "\";\"" \
                                    + str(c.flesch_kincaid_grade_level()) \
                                    + "\";\""\
                                    + str(c.coleman_liau_index())\
                                    + "\"\n"

                index_file.write(index_output_line)

        output_file.close()
        index_file.close()

        print "End testing..."
        # Stop testing