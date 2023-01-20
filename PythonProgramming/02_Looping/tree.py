# Get the number of rows for the tree
tree_height = input("How tall is the tree: ")
# Convert into an integer
tree_height = int(tree_height)
# Get the starting spaces or the top of the tree
spaces = tree_height - 1
# There is one hash to start that will be increamented
hashes  = 1
# Save stump spaces till later
stump_spaces = tree_height - 1
# Makesure the right number of rows are printed
while tree_height != 0:
# Print the spaces
    for i in range(spaces):
        print(' ', end="")
# Print the hashes
    for i in range(hashes):
        print('#', end="")
# New line after each row is printed
    print()
# That spaces is decreamented by 1 each time
    spaces -= 1
# That hashes is increamented by 2 each time
    hashes += 2
# Decreament tree height each time to jump out of the loop
    tree_height -= 1
# Print the spaces before the stamp and then the hash
for i in range(stump_spaces):
    print(' ', end="")
print("#")


