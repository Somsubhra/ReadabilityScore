from Calculator import *
from Generator import *
from os import walk, path, stat, mkdir


# The Runner class
class Runner:

    # Constructor for the runner class
    def __init__(self, input_directory, output_directory):
        self.input_directory = input_directory
        self.output_directory = output_directory

    # The main running method for the runner
    def run(self):

        asl = []
        awl = []
        asw = []
        psw = []
        psw30 = []
        juk = []

        difficulty = {}
        difficulty_scores = []

        lines = open('manual_difficulty_scores').readlines()

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

        # Write to output file
        output_file = open(path.join(self.output_directory, 'result.csv'), 'w+')
        output_file.write("\"Filename\";\"ASL\";\"AWL\";\"ASW\";\"PSW\";\"PSW30\";\"JUK\"\n")

        english_index_file = open('out/english_index.csv', 'w+')
        english_index_file.write("\"Filename\";\"Automatic Readability Index\";"
                                 "\"Gunning Fog Index\";\"Smog Index\";\"Flesch Reading Ease\";"
                                 "\"Flesch Kincaid Grade Level\";\"Coleman Liau Index\"\n")

        # Walk through all files in tree
        for (dir_path, _, file_names) in walk(self.input_directory):
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
                    psw.append(p.number_of_polysyllables())
                    psw30.append(p.number_of_polysyllables_per_30_sentences())
                    juk.append(p.number_of_jukthakshar())

                # The output line
                output_line = "\"" + str(test_file) \
                              + "\";\"" \
                              + str(p.average_sentence_length())\
                              + "\";\"" \
                              + str(p.average_word_length())\
                              + "\";\"" \
                              + str(p.average_syllable_per_word()) \
                              + "\";\""\
                              + str(p.number_of_polysyllables()) \
                              + "\";\"" \
                              + str(p.number_of_polysyllables_per_30_sentences()) \
                              + "\";\""\
                              + str(p.number_of_jukthakshar())\
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

        g = Generator(asl, awl, asw, psw, psw30, juk, difficulty_scores, self.output_directory)
        g.generate()