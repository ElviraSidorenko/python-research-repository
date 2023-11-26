# Computes the sum of the first n positive integers like sum = 1 + 2 + 3 + ... + n

# Get the input
n = int(input('Type a positive number: '))
i = 1
sum = 0

# Validate and get a positive number
while n <= 0:
    n = int(input('Your number is not valid. Try again: '))

while i <= n:
    sum = sum + i
    i += 1

# Display the result
print(sum)
