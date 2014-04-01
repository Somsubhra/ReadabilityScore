from Parser import *


# The index calculator class
class Calculator:
    def __init__(self, filename):
        self.parser = Parser(filename)