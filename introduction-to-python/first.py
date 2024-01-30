# Let's start to the very beginning ... the fundamentals

# Basic arithmetic operations
print(1 + 1)
print(2 - 1)
print(2 * 2)
print(4 / 2)

#Creating a variable
savings = 100
print(savings)

#_______________________________________________________________
#Here's a situation
# Create the variables monthly_savings and num_months
monthly_savings = 10
num_months = 4


# Multiply monthly_savings and num_months
new_savings = monthly_savings * num_months

# Add new_savings to your savings
total_savings = new_savings + savings

# Print total_savings
print("Your total savings are: ", total_savings)

#_______________________________________________________________
#Here's another situation that tells you how to show the type of a variable
words = "Hello World"
numbers = 12345
floatNumbers = 123.45

print(type(words))
print(type(numbers))
print(type(floatNumbers))

#_______________________________________________________________
#Here's another situation that shows you how to convert a variable type ==> str(), int(), float()
# Definition of savings and total_savings
savings = 100
total_savings = 150

# Fixing the printout by converting total_savings and savings to a string
print("I started with $" + str(savings) + " and now have $" + str(total_savings) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)

#Important Tip: You can't concatenate strings with numbers, you need to convert the numbers to strings first, using the str() function, and vice versa.