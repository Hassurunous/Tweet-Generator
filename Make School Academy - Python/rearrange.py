# Import random for random rearrange
import random

# Import sys to exit function is 'quit' command given.
import sys


# Function will accept any number of words, seperated by spaces, and rearrange
# them randomly.
def rearrange(string_in):
    words = []
    for word in string_in.split():
        words.append(word)
    new_words = []
    i = len(words)
    for index in range(i):
        new_words.append(words.pop(random.randrange(len(words))))
    return new_words


# Accept input from user only if the current process is __main__
if __name__ == '__main__':
    # Ask user for name of file to open.
    f = input("List of words to rearrange? (Type 'quit' to exit.)\n")

    # Run dictionaryFill on that file.
    if f == "quit":
        sys.exit()
    else:
        rearranged = rearrange(f)
        print(rearranged)
