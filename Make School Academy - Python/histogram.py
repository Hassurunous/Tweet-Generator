# Import operator for sorting dictionary at the end.
import operator

# Import sys for system functions
import sys

# Import string for string operations
import string


# Function takes in a file and splits it into its words.
# Then function stores those words in dictionary, keeping a count
# of each word, rather than storing a word multiple times.
def dictionaryFill(filename):
    # Create empty dictionary to store words from the document.
    dictionary = {}
    # Translator holds the argument information we will need to remove
    # punctuation from the words when we use .translate
    translator = str.maketrans('', '', string.punctuation)
    # Use 'with' to also close file when the function is complete
    with open(filename) as f:
        # Split the file into its lines
        for line in f:
            # Split the line into its words
            for word in line.split():
                # Take the word, remove the punctuation, and lowercase it
                word = word.translate(translator).lower()
                # If the word is already in dictionary, then increment,
                # otherwise add it to the dictionary
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
    # Return the full dictionary
    return dictionary


def uniqueWords(histogram):
    uniqueWords = 0
    for key in histogram:
        uniqueWords += 1
    return uniqueWords


def frequency(filename, word):
    dictionary = dictionaryFill(filename)
    return dictionary[word] if word in dictionary else 0


# Sort the dictionary by how many of each word were present in the file.
def dictionary_sort(dictionary):
    sorted_dictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
    # Print the sorted dictionary, now a list of tuples.
    print(sorted_dictionary)


# # Run the dictionaryFill function
# dictionaryFill("spacexarticle")

# # Ask user for name of file to open.
if __name__ == '__main__':
    f = input("BUILD a dictionary from a file, COUNT words in the file, or find FREQUENCY of a word? (Type 'quit' at any time to exit.)\n")

    # Run dictionaryFill on that file.
    if type(f) == str:
        if f == "quit":
            sys.exit()
        elif f.lower() == "build":
            f = input("What is the name of the file you wish to open?\n")
            if f == "quit":
                sys.exit()
            else:
                print(dictionaryFill(f))
        elif f.lower() == "count":
            f = input("What is the name of the file you wish to open?\n")
            if f == "quit":
                sys.exit()
            else:
                print("There are", uniqueWords(dictionaryFill(f)), "words in this file.")
        elif f.lower() == "frequency":
            f = input("What is the name of the file you wish to open?\n")
            if f == "quit":
                sys.exit()
            else:
                g = input("What word are you looking for in the file?\n")
                if g == "quit":
                    sys.exit()
                else:
                    print("The word", g, "shows up", frequency(f, g), "times in the file.")
    else:
        print("Must input a file name as string.")
        sys.exit()
