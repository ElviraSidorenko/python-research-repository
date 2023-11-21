# Prints multiples of p from 10 until the value of q (inclusive)

# Get the inputs
m = int(input('Get multiples of: '))
q = int(input('Until: '))


i = 10
list = ''

while i <= q:
    if (i % m) == 0:
        list = list + f"{i},"
        i += 1
    else:
        i += 1


# Display results
print(list)
