# - Order matter in the tuple
# - You cannot modify (append or add things) the tuple
# - They're memory efficient
# - Good for storing lots of little things, like X Y coordinates

my_tuple = (1, 2, 3)
print(len(my_tuple))

(1, 2) == (2, 1)  # False

my_tuple.append(4)  # AttributeError: 'tuple' object has no attribute 'append'
