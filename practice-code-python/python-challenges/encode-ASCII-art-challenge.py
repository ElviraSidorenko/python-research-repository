# Task:   Encodes a string like 'AAAAABBBBAAA' as a list of tuples: [('A', 5), ('B', 4), ('A', 3)]


def encodeString(stringVal):
    encodedList = []
    prevChar = stringVal[0]
    count = 0
    for char in stringVal:
        if prevChar != char:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1

    encodedList.append((prevChar, count))
    return encodedList


# Takes in a list of tuples and prints the original string

def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr
