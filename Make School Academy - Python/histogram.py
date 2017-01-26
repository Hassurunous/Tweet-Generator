# Import operator for sorting dictionary at the end.
import operator

# Create empty dictionary to store words from the document.
dictionary = {}


# Function takes in a file and splits it into its words.
# Then function stores those words in dictionary, keeping a count
# of each word, rather than storing a word multiple times.
def dictionaryFill(file):
    with open(file) as f:
        for line in f:
            for word in line.split():
                word.lower()
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
    # Sort the dictionary by how many of each word were present in the file.
    sorted_dictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)

    # Print the sorted dictionary, now a list of tuples.
    print(sorted_dictionary)


# # Run the dictionaryFill function
# dictionaryFill("spacexarticle")

# Ask user for name of file to open.
f = input("Name of file to open?\n")

# Run dictionaryFill on that file.
dictionaryFill(f)
