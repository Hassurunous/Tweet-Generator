import random

# file = open("sample_dict.txt")
# words = []

# for line in iter(file):
#     words.append(line.rstrip('\n'))
#     print(words)
#
# file.close

# Refactored based on stackoverflow answer discovered while researching.
# with open("sample_dict.txt") as f:
#     words = f.read().splitlines()

# file.close

# print(words)

# Refactored again to remove need to store array of all words in dictionary.
# Lists 5 random lines from chosen file now.

# Updated to read from full dictionary. Still reads 5 values.

file = open("dictionary")
words = []

f = file.read().splitlines()

for word in range(5):
    print(random.choice(f))

file.close()
