# Challenge: Write a Python program that converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None

# Dictionary mapping hexadecimal characters to their decimal values
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}


# Function to convert a hexadecimal number to its decimal equivalent
def hexToDec(hexNum):
    # Check if each character in the input is a valid hexadecimal character
    for letter in hexNum:
        if letter not in hexNumbers:
            # If any character is not valid, return None
            return None

    # Conversion based on the length of the hexadecimal number
    if len(hexNum) == 1:
        return hexNumbers[hexNum]
    if len(hexNum) == 2:
        # For a two-digit hexadecimal number, calculate the decimal equivalent
        return hexNumbers[hexNum[0]] * 16 + hexNumbers[hexNum[1]]
    if len(hexNum) == 3:
        # For a three-digit hexadecimal number, calculate the decimal equivalent
        return hexNumbers[hexNum[0]] * 256 + hexNumbers[hexNum[1]] * 16 + hexNumbers[hexNum[2]]


# Get a hexadecimal number from the user
hex_input = input('Type a hexadecimal number: ')


# Display the result of the hexToDec function
print(hexToDec(hex_input))
