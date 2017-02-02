# Import out Histogram program
from histogram import dictionaryFill

# Import random for a random number
import random

# Import operator for dictionary sort.
import operator

# Import sys to exit if 'quit' given
import sys


# This function returns a random key from the dictionary of words
# Dictionary is filled based on the input file
def dictionaryRandom(filename):
    dictionary = list(dictionaryFill(filename))
    return dictionary[random.randrange(0, len(dictionary))]


# This function returns a random key from the dictionary, weighted by the
# number of times the word appears in the seeded file.
# Dictionary is filled based on the input file.
def dictionaryRandomWeighted(filename):
    dictionary = dictionaryFill(filename)
    weighted_dictionary = []
    for key, value in dictionary.items():
        for item in range(value):
            weighted_dictionary.append(key)
    return weighted_dictionary[random.randrange(0, len(weighted_dictionary)-1)]


# This function sorts a dictionary based on the values of each key
def dictionarySort(dict):
    return sorted(dict.items(), key=operator.
                  itemgetter(1), reverse=True)


if __name__ == '__main__':
    # Ask user if they want a 'pure' random sample or weighted random
    f = input("Fully random or weighted random? (Type 'quit' to exit.)\n")

    # Quit if command 'quit' given, else run selected random
    if f == "quit" or f == "":
        sys.exit()
    elif f.lower() == "fully" or f.lower() == "fully random":
        # Ask user for file name
        f = input("What is the name of the file? (Type 'quit' to exit.)\n")
        # Check to make sure that the user has input a string
        if type(f) == str:
            # Print word returned by dictionaryRandom()
            print(dictionaryRandom(f))
        else:
            # Print an error message
            print("Function dictionaryRandom requires a string input.")
    elif f.lower() == "weighted" or f.lower() == "weighted random":
        # Ask user for file name
        f = input("What is the name of the file? (Type 'quit' to exit.)\n")
        # Check to make sure that the user has input a string
        if type(f) == str:
            # Print word returned by dictionaryRandomWeighted()
            print(dictionaryRandomWeighted(f))
        else:
            # Print an error message.
            print("Function dictionaryRandomWeighted requires a string input.")
