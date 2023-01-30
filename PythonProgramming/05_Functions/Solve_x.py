#   X + 4 = 9
# Receive the string and split the string into variables
def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()

    num1, num2 = int(num1), int(num2)
    return "x = " + str(num2 - num1)

print(solve_eq("x + 4 = 9"))
# Convert the strings into ints
# Convert the result into a string and join it to the string "X = "
# Print ()