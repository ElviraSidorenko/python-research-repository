# The term "casting" refers to the process of converting a value from one data type to another.
# Casting can be explicit, where you specify the conversion, or implicit, where the programming language automatically handles the conversion under certain circumstances.

# Implicit casting (automatic)
x = 5      # x is an integer
y = 2.5    # y is a floating-point number
z = x + y  # Python automatically casts x to a float for the addition
print(z)   # This will print 7.5, the result of adding 5 (int) and 2.5 (float)

# Explicit casting
a = 10.6   # a is a float
b = int(a)  # Explicitly casting the float 'a' to an integer
print(b)   # This will print 10, as the decimal part is truncated in the conversion
