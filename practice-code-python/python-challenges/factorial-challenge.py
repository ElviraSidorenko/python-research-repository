# Challenge: Write a Python program that returns the value of the factorial of num if it is defined

def factorial(num):
    # Check if the input is non-empty and can be converted to an integer
    if num:
        try:
            # Convert the input to an integer
            int_number = int(num)
        except ValueError:
            # If conversion fails, return an error message
            return 'Not a number'
    else:
        # If the input is empty, return None
        return None

    # Handle the case where the input is 0
    if int_number == 0:
        return 1

    # Calculate the factorial using a loop
    total = 1
    while int_number > 1:
        total = total * int_number
        int_number = int_number - 1

    # Return the calculated factorial
    return total


# Get a number from the user
number = input('Type a number: ')

# Display the result
print(factorial(number))
