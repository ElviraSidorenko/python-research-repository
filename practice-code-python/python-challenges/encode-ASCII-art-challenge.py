# Challenge: Write a Python program that encodes a string like 'AAAAABBBBAAA' as a list of tuples: [('A', 5), ('B', 4), ('A', 3)] and has a function to decode it back.

# Encode a string by counting consecutive occurrences of each character
def encodeString(stringVal):
    # Initialize an empty list to store the tuples (character, count)
    encodedList = []
    # Initialize variables to track the previous character and its count
    prevChar = stringVal[0]
    count = 0

    # Iterate through each character in the input string
    for char in stringVal:
        # Check if the current character is different from the previous one
        if prevChar != char:
            # Append a tuple to the encoded list with the previous character and its count
            encodedList.append((prevChar, count))
            # Reset the count for the new character
            count = 0
        # Update the previous character
        prevChar = char
        # Increment the count for the current character
        count = count + 1

    # Append the last character and its count to the encoded list
    encodedList.append((prevChar, count))
    # Return the list of tuples representing the encoded string
    return encodedList


# Decode a list of tuples into the original string
def decodeString(encodedList):
    # Initialize an empty string to store the decoded string
    decodedStr = ''

    # Iterate through each tuple in the input list
    for item in encodedList:
        # Append to the decoded string the character repeated by its count
        decodedStr = decodedStr + item[0] * item[1]

     # Return the decoded string
    return decodedStr
