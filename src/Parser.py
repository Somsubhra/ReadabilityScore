class Parser:
    def __init__(self, filename):
        self.filename = filename
        self.contents = open(filename).read()
        self.contents = self.contents.decode("utf-8")

        self.words = self.contents.split()
        self.number_of_words = len(self.words)