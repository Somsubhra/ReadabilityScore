# Parser class
class Parser:

    # Constructor for parser class
    def __init__(self, filename):
        self.filename = filename

        # Read the contents of file as UTF-8
        self.contents = open(filename).read()
        self.contents = self.contents.decode("utf-8")

        self.words = self.contents.split()

    # Number of words in the content
    def number_of_words(self):
        return len(self.words)

    # Number of sentences in the content
    def number_of_sentences(self):
        number = 0

        separators = [u".", u"!", u"?"]

        for word in self.words:
            if word[-1] in separators and len(word) > 1:
                number += 1

        return number
