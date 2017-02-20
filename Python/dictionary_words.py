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

# Updated to read a number of words specified by the user.

file = open("dictionary")
words = []

f = file.read().splitlines()

num = int(input("How many words would you like to display?\n"))

for word in range(num):
    print(random.choice(f), end=" ")

print()

file.close()
