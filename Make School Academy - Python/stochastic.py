# Import out Histogram program
from histogram import dictionaryFill

# Import random for a random number
import random

# Import operator for dictionary sort.
import operator

# Import sys to exit if 'quit' given
import sys

# Import timeit to test code runtime
from timeit import Timer


# This function returns a random key from the dictionary of words
# Dictionary is filled based on the input file
def dictionaryRandom(filename):
    dictionary = list(dictionaryFill(filename))
    return dictionary[random.randrange(0, len(dictionary))]


# This function returns a random key from the dictionary, weighted by the
# number of times the word appears in the seeded file.
# Dictionary is filled based on the input file.
# Inefficient function creates an array. Refactoring for efficiency.
def dictionaryRandomArray(dictionary):
    weighted_dictionary = []
    for key, value in dictionary.items():
        for item in range(value):
            weighted_dictionary.append(key)
    return weighted_dictionary[random.randrange(0, len(weighted_dictionary)-1)]


def dictionaryRandomWeighted(dictionary):
    # Create an indexed list of tuples from the dictionary
    word_list = list(dictionary.items())
    # Find the total number of words in the dictionary
    word_range = sum(dictionary.values())
    target = random.randrange(0, word_range - 1)
    # Count and Index used to iterate through list to find word matching
    # the target number, based on the values. Much like a number line.
    count = 0
    index = 0
    # Iterate through the list of words until you reach the target number
    # and increment your counter based on the value of each key in the
    # dictionary, now a list of tuples
    while(count < target):
        # Add the value of the current word to the ongoing counter
        count += word_list[index][1]
        # If the value of count is still below the target, increment index
        if(count < target):
            index += 1
    else:
        # When the loop finds the word, return the word
        return(word_list[index][0])


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
        f = input("Random word by converting to ARRAY or from word WEIGHT?( Type 'quit' to exit.)\n")
        if f.lower() == "array" or f.lower() == "converting to array":
            # Ask user for file name
            f = input("What is the name of the file? (Type 'quit' to exit.)\n")
            # Check to make sure that the user has input a string
            if type(f) == str:
                # Print word returned by dictionaryRandomWeighted()
                dictionary = dictionaryFill(f)
                t = Timer("""dictionaryRandomArray(dictionary)""", setup="from __main__ import dictionaryRandomArray, dictionary")
                print("Run time from 100 runs =", t.timeit(100))
                print("Your word is: ", dictionaryRandomArray(dictionary))
            else:
                # Error message or quit command
                print("'Quit' or invalid input detected. Quitting program...")
                sys.exit()
        if f.lower() == "weight" or f.lower() == "word weight":
            # Ask user for file name
            f = input("What is the name of the file? (Type 'quit' to exit.)\n")
            # Check to make sure that the user has input a string
            if type(f) == str:
                # Fill dictionary with words from file given
                dictionary = dictionaryFill(f)
                # Print word returned by dictionaryRandomWeighted()
                t = Timer("""dictionaryRandomWeighted(dictionary)""", setup="from __main__ import dictionaryRandomWeighted, dictionary")
                print("Run time from 100 runs =", t.timeit(100))
                print("Your word is:", dictionaryRandomWeighted(dictionary))
            else:
                # Error message or quit command
                print("'Quit' or invalid input detected. Quitting program...")
                sys.exit()
        else:
            # Error message or quit command
            print("'Quit' or invalid input detected. Quitting program...")
            sys.exit()
