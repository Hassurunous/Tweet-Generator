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
def dictionary_random(filename):
    dictionary = list(dictionaryFill(filename))
    return dictionary[random.randrange(0, len(dictionary))]


# This function returns a random key from the dictionary, weighted by the
# number of times the word appears in the seeded file.
# Dictionary is filled based on the input file.
# Inefficient function creates an array. Refactoring for efficiency.
def dictionary_random_array(dictionary):
    weighted_dictionary = []
    for key, value in dictionary.items():
        for item in range(value):
            weighted_dictionary.append(key)
    return weighted_dictionary[random.randrange(0, len(weighted_dictionary))]


# This function converts the dictionary to a list of tuples, then searches
# through the list, counting all instances of each word in the list, until
# the count reaches the target random value.
def dictionary_random_weighted(dictionary):
    # Create an indexed list of tuples from the dictionary
    # word_list = list(dictionary.items())
    # Create a sorted iterator object, instead of list, to preserve memory
    word_list = dictionary.items()
    # print("Word List =", word_list)
    # Find the total number of words in the dictionary
    word_range = sum(dictionary.values())
    # Find a random target in the range
    target = random.randrange(1, word_range + 1)
    # Count and Index used to iterate through list to find word matching
    # the target number, based on the values. Much like a number line.
    count = 0
    # Iterate through the list of words until you reach the target number
    # and increment your counter based on the value of each key in the
    # dictionary, now a list of tuples.
    for word, frequency in word_list:
        count += frequency
        # If the count has become larger than the target number, return the
        # word you are now on, otherwise continue the loop
        if(count >= target):
            # print("Final Target, Range, Count, Word = (", target, ",", word_range, ",", count, ",", word, ")")
            return word
        # print("Target, Range, Count, Word = (", target, ",", word_range, ",", count, ",", word, ")")


# This function sorts a dictionary based on the values of each key
def dictionary_sort(dict):
    return sorted(dict.items(), key=operator.
                  itemgetter(1), reverse=True)


# Test functions for correct level of randomness
test_dictionary = dictionaryFill("testpage")


def random_function_validation(function_name):
    words_counter = {}
    if(function_name == dictionary_random_weighted) or (function_name == dictionary_random_array) or (function_name == dictionary_random):
        for count in range(10000):
            word = function_name(test_dictionary)
            if word in words_counter:
                words_counter[word] += 1
            else:
                words_counter[word] = 1
    return words_counter


# Run test function for each function to test for randomness
# print("dictionary_random_array return =", random_function_validation(dictionary_random_array))
# print("dictionary_random_weighted return =", random_function_validation(dictionary_random_weighted))


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
                t = Timer("""dictionary_random_array(dictionary)""", setup="from __main__ import dictionary_random_array, dictionary")
                print("Run time from 100 runs =", t.timeit(100))
                print("Your word is: ", dictionary_random_array(dictionary))
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
                t = Timer("""dictionary_random_weighted(dictionary)""", setup="from __main__ import dictionary_random_weighted, dictionary")
                print("Run time from 100 runs =", t.timeit(100))
                print("Your word is:", dictionary_random_weighted(dictionary))
            else:
                # Error message or quit command
                print("'Quit' or invalid input detected. Quitting program...")
                sys.exit()
        else:
            # Error message or quit command
            print("'Quit' or invalid input detected. Quitting program...")
            sys.exit()
