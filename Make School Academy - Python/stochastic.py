# Import out Histogram program
from histogram import dictionaryFill

# Import random for a random number
import random

# Import operator for dictionary sort.
import operator

# Import sys to exit if 'quit' given
import sys

if __name__ == '__main__':
    # Build a dictionary from the function "dictionaryFill(filename)"" in
    # histogram.py and sort those values for indexing.
    # Ask user for name of file to open.
    f = input("Name of file to open? (Type 'quit' to exit.)\n")

    # Run dictionaryFill on that file.
    if f == "quit":
        sys.exit()
    else:
        dictionary = dictionaryFill(f)

    sorted_dictionary = sorted(dictionary.items(), key=operator.itemgetter(1),
                               reverse=True)

    print(sorted_dictionary[random.randrange(0, len(dictionary))])
