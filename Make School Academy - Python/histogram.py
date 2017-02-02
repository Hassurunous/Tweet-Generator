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
    with open(filename) as f:
        translator = str.maketrans('', '', string.punctuation)
        for line in f:
            for word in line.split():
                word = word.translate(translator).lower()
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
    return dictionary


# # Run the dictionaryFill function
# dictionaryFill("spacexarticle")

# # Ask user for name of file to open.
if __name__ == '__main__':
    f = input("Name of file to open? (Type 'quit' to exit.)\n")

    # Run dictionaryFill on that file.
    if f == "quit":
        sys.exit()
    else:
        dictionary = dictionaryFill(f)

    # Sort the dictionary by how many of each word were present in the file.
    sorted_dictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)

    # Print the sorted dictionary, now a list of tuples.
    print(sorted_dictionary)
