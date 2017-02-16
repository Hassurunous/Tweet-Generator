# Import system library to take input
import sys

# Import string for string operations
import string

# Import Dictogram.py for Dicotgram class
from Dictogram import Dictogram


"""
Pseudo Code:

1. Take in a list of words or characters.
2. For the first element of the Dictogram 'markov_model', insert a key into the
markov_model equal to the element, then set its value equal to a Dictogram.
2a. The Dictogram should be a list of words and occurences of that word.

"""


def build_markov_model(data):
    print(data)
    # Going to build a dictionary with unique words as keys and a Dictogram of
    # any words that follow that word as the value
    markov_model = Dictogram()
    for index, item in enumerate(data):
        if item in markov_model:
            if index+1 == len(data):
                markov_model[item].update(["END"])
            else:
                markov_model[item].update([data[index + 1]])
        else:
            if index+1 == len(data):
                markov_model[item] = Dictogram(["END"])
            else:
                markov_model[item] = Dictogram([data[index + 1]])
    return markov_model


def make_markov_model(data):
    markov_model = Dictogram()

    for i in range(0, len(data)-1):
        if data[i] in markov_model:
            # We have to just append to the existing histogram
            markov_model[data[i]].update([data[i+1]])
        else:
            markov_model[data[i]] = Dictogram([data[i+1]])
    return markov_model


if __name__ == "__main__":
    print(sys.argv[1:])
    markov = build_markov_model(sys.argv[1:])
    print(markov)
    print(markov.random_word())
