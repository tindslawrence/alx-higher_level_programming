# Ask for a string
orig_string = input("Convert to Acronym: ")
# Convert the string into uppercase
orig_string = orig_string.upper()
# Convert the string into a list
list_of_words = orig_string.split()
# Cylce through the list
for word in list_of_words:
    
# Get the first letter of the word and eliminate the newline
    print(word[0], end="")
# Add a newline
print()