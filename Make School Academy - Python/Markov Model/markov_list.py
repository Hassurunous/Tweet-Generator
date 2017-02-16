# Import system library to take input
import sys

# Import string for string operations
import string

# Import Dictogram.py for Dicotgram class
from Dictogram import Dictogram


def build_markov_model(data):
    # Going to build a dictionary with unique words as keys and a Dictogram of
    # any words that follow that word as the value
    markov_model = {}
    for index, item in enumerate(data):
        if data[index] in markov_model:
            markov_model[data[index]].update(data[index+1])
        else:
            markov_model[data[index]] = Dictogram(data[index+1])
    return markov_model


if __name__ == "__main__":
    print(sys.argv[:1])
    build_markov_model(sys.argv[0:])
