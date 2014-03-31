from Parser import *
from os import walk, path, stat, mkdir


# The Runner class
class Runner:

    # Constructor for the runner class
    def __init__(self, input_directory, output_directory):
        self.input_directory = input_directory
        self.output_directory = output_directory

    # The main running method for the runner
    def run(self):
        f = []
        for (dir_path, _, file_names) in walk(self.input_directory):
            for filename in file_names:
                test_file = path.join(dir_path, filename)
                p = Parser(test_file)
                try:
                    stat(self.output_directory)
                except:
                    mkdir(self.output_directory)
