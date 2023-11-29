# Challenge: write a Python program that takes a number as input from the user and then prints a sequence of numbers enclosed in square brackets up to the given input number.

# Prompt the user to enter a number, convert the input to an integer, and assign it to the variable n.
n = int(input('Type a number: '))
result_str = ''

# Ensure a valid number is provided
while n <= 0:
    n = int(input('Not a valid number. Try again.'))

# Concatenate square bracketed numbers to the result string
i = 1
while i <= n:
    result_str = result_str + f'[{i}]'
    i += 1


# Display the result
print(result_str)
