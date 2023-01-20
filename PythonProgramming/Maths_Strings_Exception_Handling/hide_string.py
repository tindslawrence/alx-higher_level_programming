# Input "Enter the string to hide in uppercase"
norm_string = input("Enter string to hide in uppercase : ")

secret_string = ""
# Cycle through each character in the string
for char in norm_string: 
# Store each character code i a new string
    secret_string += str(ord(char) -23)
# Print "Secret Message"
print("Secret Message : ", secret_string)
# Cycle through each character code 2 at a time by incrementing by 2 each time
norm_string = ""
for i in range(0, len(secret_string)-1, 2):
# Get the 1st and 2nd for the digit number
    char_code = secret_string[i] + secret_string[i+1]
# Convert the code into characters and add them to a new string
    norm_string += chr(int(char_code) + 23)
# Print Original Message: 
print("Original Message: ", norm_string)