# Creating an integer from a string:

num_str = "42"
num_int = int(num_str)


# Converting a floating-point number to an integer (truncating the decimal part):

float_num = 3.14
int_num = int(float_num)  # Result: 3


# Specifying the base for integer conversion (e.g., converting a binary string to an integer):

binary_str = "1010"
decimal_num = int(binary_str, 2)  # Result: 10 (base 2)


# Creating an integer from a Boolean value (True becomes 1, and False becomes 0):

bool_value = True
int_value = int(bool_value)  # Result: 1
