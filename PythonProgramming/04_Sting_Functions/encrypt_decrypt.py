# Receive the message to encypt and the number of characters to shift
message = input("Enter your message: ")
key = int(input("How many characters should we shift (1 - 26): "))
# Prepare the secret message
secret_message = ""
# Cycle through each character in the message
for char in message:
# If it isnt a letter, then keep it as it is
    if char.isalpha():
# Get the character code and add the shift amount
        char_code = ord(char)
        char_code += key
# If uppercase then compare the upercase unicodes
        if char.isupper():
# If bigger than Z subtract 26
            if char_code > ord('Z'):
                char_code -= 26
# If smaller that A add 26
            if char_code < ord('A'):
                char_code += 26
# Do the same for the lower case characters
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26


# Convert from code to letter and to message
        secret_message += chr(char_code)
    else:
        secret_message += char
print("Encrypted : ", secret_message)
# If not a letter leave character as is
# To decrypt the only thing that changes is the sign of the key
key = -key
orig_message = ""
# The same as above
for char in secret_message:
# If it isnt a letter, then keep it as it is
    if char.isalpha():
# Get the character code and add the shift amount
        char_code = ord(char)
        char_code += key
# If uppercase then compare the upercase unicodes
        if char.isupper():
# If bigger than Z subtract 26
            if char_code > ord('Z'):
                char_code -= 26
# If smaller that A add 26
            if char_code < ord('A'):
                char_code += 26
# Do the same for the lower case characters
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26


# Convert from code to letter and to message
        orig_message += chr(char_code)
    else:
        orig_message += char
print("Decrypted : ", orig_message)
