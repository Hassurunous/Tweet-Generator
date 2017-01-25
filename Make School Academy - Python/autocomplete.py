# Open file and declare array to store any words discovered as autocompletes.
file = open("dictionary")
words = []

# Split file into lines for easy searching.
f = file.read().splitlines()

# Get input from user to figure out what to autocomplete.
letters = input("Enter the letters you would like to autocomplete:\n")

# Search through dictionary for words that begin with the string provided.
for line in f:
    if line[:(len(letters))] == letters:
        words.append(line)

# Display list of words that the input could autocomplete to.
for word in words:
    print(word)
