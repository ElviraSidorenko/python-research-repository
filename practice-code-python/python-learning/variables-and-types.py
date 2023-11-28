# - Variables name cannot start with numbers
# - Variables name cannot contain any special characters except for an underscore
# - When creating a variable name with more than two words use _ symbol to represent a space
# - Variable names start with lowercase letters; never start a variable name with an uppercase letter (it could be confused with a class)

# Integer variable
age = 25

# Float variable
height = 5.9

# String variable
full_name = "John Doe"

# Boolean variable
is_student = True

# List variable
grades = [90, 85, 92, 88, 95]

# Tuple variable
coordinates = (10.0, 20.5)

# Dictionary variable
person_info = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Set variable
hobbies = {'reading', 'traveling', 'photography'}

# NoneType variable
temp_variable = None

# Complex variable
complex_number = 3 + 2j

# Custom class variable


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person_object = Person("Bob", 28)


# You can check types of variables by using type() function:
print(type(age))
print(type(height))
print(type(full_name))
print(type(is_student))
print(type(grades))
print(type(coordinates))
print(type(person_info))
print(type(hobbies))
print(type(temp_variable))
print(type(complex_number))
print(type(person_object))
