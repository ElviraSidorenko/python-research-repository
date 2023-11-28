# Dictionary - a set of key: value pairs, with the requirement that the keys are unique (within one dictionary).
# Order does not matter

my_dictionary = {
    'apple': 'A red fruit',
    'bear': 'A big animal',
}

my_dictionary['apple']  # Out: 'A red fruit'

# Trailing comma at the end of the last pair in the dictionary
# It is useful because then every line has the same format and adding entries to the end is the same as adding them to the middle.
# It also prevents the frequent bug of writing

animals = {
    'a': 'aardvark',
    'b': 'bear',
    'c': 'cat',
}

# Available methods:

# The keys() method returns a view of all keys in the dictionary.
print(animals.keys())  # Out: dict_keys(['a', 'b', 'c'])

# The values() method returns a view of all values in the dictionary.
print(animals.values())  # Out: dict_values(['aardvark', 'bear', 'cat'])

# The get() method is used to retrieve the value associated with a specified key.
# If the key is not found, it returns the specified default value (or None if not provided).
print(animals.get('a'))  # Out: aardvark

# The len() function returns the number of items (key-value pairs) in a dictionary.
print(len(animals))  # Out: 3


# Adding to the dictionary
creatures = {
    'a': ['aardvark', 'antelope'],
    'b': ['bear'],
}

creatures['b'].append('bison')

if 'c' not in creatures:
    creatures['c'] = []

creatures['c'].append('cat')

# Resources:
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# https://www.w3schools.com/python/python_dictionaries.asp
# https://realpython.com/python-dicts/
# https://coderwall.com/p/4fvcaa/trailing-comma-in-python-data-structures
