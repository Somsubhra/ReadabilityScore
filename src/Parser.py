# Parser class
class Parser:

    # Constructor for parser class
    def __init__(self, filename):
        self.filename = filename

        # Read the contents of file as UTF-8
        self.contents = open(filename).read()
        self.contents = self.contents.decode("utf-8")

        # Store all words of content
        self.words = self.contents.split()

        # Calculate number of words
        self.no_words = len(self.words)

        # Calculate number of sentences
        self.no_sentences = 0

        # Calculate the average word length
        self.avg_word_l = 0

        separators = [u".", u"!", u"?"]

        for word in self.words:
            if word[-1] in separators and len(word) > 1:
                self.no_sentences += 1
            self.avg_word_l += float(len(word)) / float(self.no_words)

        if self.no_sentences == 0:
            self.no_sentences = 1

    # Number of words in the content
    def number_of_words(self):
        return self.no_words

    # Number of sentences in the content
    def number_of_sentences(self):
        return self.no_sentences

    # Average number of words per sentence
    def average_words_per_sentence(self):
        return float(self.no_words) / float(self.no_sentences)

    # Average word length
    def average_word_length(self):
        return self.avg_word_l
