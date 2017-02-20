# Import system library to take input
import sys

# Import Dictogram.py for Dicotgram class
from Dictogram import Dictogram

# Import listFill from histogram.py
from histogram import listFill


"""
Pseudo Code:

1. Take in a list of words or characters.
2. For the first element of the Dictogram 'markov_model', insert a key into the
markov_model equal to the element, then set its value equal to a Dictogram.
2a. The Dictogram should be a list of words and occurences of that word.

"""


def build_markov_model(data):
    # Going to build a dictionary with unique words as keys and a Dictogram of
    # any words that follow that word as the value
    markov_model = Dictogram()
    for index, item in enumerate(data):
        if item in markov_model:
            if index+1 == len(data):
                markov_model[item].update(["[END]"])
            else:
                markov_model[item].update([data[index + 1]])
        else:
            if index == 0:
                markov_model["[END]"] = Dictogram([item])
            if index+1 == len(data):
                markov_model[item] = Dictogram(["[END]"])
            else:
                markov_model[item] = Dictogram([data[index + 1]])
    return markov_model


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        # print(sys.argv[1:])
        markov = build_markov_model(sys.argv[1:])
        # print(markov)
        print(markov.random_word())
        print(markov.generate_sentence(50))
    else:
        markov = build_markov_model(listFill("spacexarticle"))
        # print(markov)
        print(markov.random_word())
        print(markov.generate_sentence(50))
