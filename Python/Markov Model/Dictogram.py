# Import string for string operations
import string

# Import random for random sampling
import random


class Dictogram(dict):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Dictogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        # Translator holds the argument information we will need to remove
        # punctuation from the words when we use .translate
        # translator = str.maketrans('', '', string.punctuation)
        for item in iterable:
            self.tokens += 1
            # # Take the item, remove the punctuation, and lowercase it
            # item = item.translate(translator).lower()
            # If the item is already in dictionary, then increment,
            # otherwise add it to the dictionary
            if item in self:
                self[item] += 1
            else:
                self[item] = 1
                self.types += 1

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        return self[item] if item in self else 0

    def generate_sentence(self, num_of_words):
        sentence = []
        for i in range(num_of_words):
            if i == 0:
                sentence.append(self.random_word("[END]"))
            sentence.append(self.random_word(sentence[i]))
        return " ".join(sentence)

    def random_word(self, seed=None):
        if seed:
            random_word = self[seed].random_word()
            return random_word[0]
        else:
            return random.sample(self, 1)
