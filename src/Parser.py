class Parser:
    def __init__(self, filename):

        self.filename = filename

        # Read the contents of file as UTF-8
        self.contents = open(filename).read()
        self.contents = self.contents.decode("utf-8")

        # Find the words in content
        self.words = self.contents.split()

        # Find the number of words in the content
        self.number_of_words = len(self.words)