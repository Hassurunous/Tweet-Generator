
# Open file and declare array to store any words discovered as anagrams.
file = open("dictionary")
words = []

# Split file into its individual lines.
f = file.read().splitlines()

# Request user input.
letters = input("Type your letters, no spaces, and "
                "we'll try to find an anagram!\n")

# Sort user input alphabetically.
sorted_letters = ''.join(sorted(letters))

# Search through the dictionary for anagrams.
# For each line, sort that word alphabetically and compare to user unput.
for line in f:
    word = line
    print(word)
    line = ''.join(sorted(line))
    print("Sorted line = ", line)
    print("sorted_letters = ", sorted_letters)
    if sorted_letters == line:
        words.append(word)

# Print the resulting anagrams.
print("Anagrams for your letters include:")
for word in words:
    print(word)
