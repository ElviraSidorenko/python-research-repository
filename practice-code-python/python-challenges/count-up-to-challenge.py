# Get a number

n = int(input('Type a number: '))
list = ''

# Prints 1 through to n in square brackets like [1][2][3]...[n]

while n <= 0:
    n = int(input('Not a valid number. Try again.'))

i = 1
while i <= n:
    list = list + f'[{i}]'
    i += 1


# Display a result
print(list)
