# Challenge: Write a Python program that calculates the sum of all positive integers from 1 to a user-provided positive number (n).
# The program starts by prompting the user to input a positive number and validates the input to ensure it is indeed a positive integer.
# If the user provides a non-positive number, the program prompts the user to try again until a valid input is received.


# Get the input
n = int(input('Type a positive number: '))
i = 1
sum = 0

# Validate and get a positive number
while n <= 0:
    n = int(input('Your number is not valid. Try again: '))

# Compute the sum of the first n positive integers like sum = 1 + 2 + 3 + ... + n
while i <= n:
    sum = sum + i
    i += 1

# Display the result
print(sum)
