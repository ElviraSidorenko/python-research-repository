# Challenge: Write a Python program that prints multiples of p from 10 until the value of q (inclusive)

# Get user input for the multiples and the upper limit
m = int(input('Get multiples of: '))
q = int(input('Until: '))

# Initialize a variable for iteration starting from 10
i = 10
# Initialize an empty string to store the multiples
list = ''

# Iterate through numbers from 10 up to the specified upper limit (q)
while i <= q:
    # Check if the current number (i) is a multiple of the specified value (m)
    if (i % m) == 0:
        # If it is a multiple, add it to the result list
        list = list + f"{i},"
        # Increment the iterator
        i += 1
    else:
        i += 1


# Display the list of multiples
print(list)
