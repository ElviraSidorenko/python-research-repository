# In Python, list comprehensions are a concise and elegant way to create lists by applying an expression to each item in an existing iterable (e.g., a list, tuple, or range) and collecting the results in a new list.

# List comprehensions provide a more readable and compact alternative to traditional for loops when you want to generate a new list based on an existing one.

# The basic syntax of a list comprehension is as follows:

# new_list = [expression for item in iterable]

# 1. expression: This is the operation or expression that is applied to each item in the iterable. It defines what you want to include in the new list.
# 2. item: This represents the variable that takes on each value in the iterable as the loop iterates.
# 3. iterable: This is the existing sequence or iterable that you want to process.


myList = [1, 2, 3, 4, 5]
new_list = [2*item for item in myList]
print(new_list)  # Out: [2, 4, 6, 8, 10]


myList = list(range(100))
filteredList = [item for item in myList if item % 10 == 0]
print(filteredList)  # Out: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]


myString = 'My name is Elvira. I live in Auckland'


def cleanWord(word):
    return word.replace('.', '').lower()


# Out: ['my', 'name', 'is', 'elvira', 'i', 'live', 'in', 'auckland']
print([cleanWord(word) for word in myString.split()])


# List comprehensions align with several design principles that are fundamental to Python's philosophy:\

# DRY - List comprehensions help in avoiding repetitive code.
# KISS - List comprehensions are generally simple and straightforward.
# SRP - List comprehensions often encapsulate a single operation or transformation on elements, adhering to the SRP. This can lead to more modular and maintainable code.
