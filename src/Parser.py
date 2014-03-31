class Parser:
    def __init__(self, filename):
        self.filename = filename
        self.contents = open(filename).read()
        self.contents = self.contents.decode("utf-8")

    def number_of_words(self):
        words = self.contents.split()
        return len(words)