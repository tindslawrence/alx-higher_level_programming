# Have a user enter their investment amount and expected interest
# Each year their investment will increase by their investment + their investment * interest rate 
# Print out the earnings after a 10 year period
# Ask for the money invested + the interest rate
money = input("How much to invest: ")
interest_rate = input("Interest Rate: ")
# Convert the value to a float
money = float(money)
# Convert value to a float and round the percentage rate by 2 digits
interest_rate = float(interest_rate) * 0.1
# Cycle through 10 years using a for loap and rage from 0 to 9
for i in range(10):
    money = money + (money * interest_rate)
# Output the results
print("Investment after 10 years: {:.2f}".format(money))
