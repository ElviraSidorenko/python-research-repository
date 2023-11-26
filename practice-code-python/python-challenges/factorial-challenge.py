# Returns the value of the factorial of num if it is defined
def factorial(num):

    if num:
        try:
            int_number = int(num)
        except ValueError:
            return 'Not a number'
    else:
        return None
    if int_number == 0:
        return 1

    total = 1
    while int_number > 1:
        total = total * int_number
        int_number = int_number - 1

    return total


# Get a number
number = input('Type a number: ')

# Display result
print(factorial(number))
