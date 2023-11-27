# Object-oriented programming (OOP) is a programming paradigm that uses objects and classes for organizing code.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday! I am now {self.age} years old.")

# Create instances of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Access attributes and call methods
person1.introduce()
person2.introduce()

person1.celebrate_birthday()

# Check the updated age
person1.introduce()


# In this example:

# We define a Person class with an __init__ method (constructor) to initialize the object's attributes (name and age).
# The introduce method prints a simple introduction using the object's attributes.
# The celebrate_birthday method increments the person's age and prints a birthday message.
# We create two instances of the Person class (person1 and person2) and manipulate their attributes and call their methods.


# Resources:
# https://medium.com/@rogercodes1/what-is-object-oriented-programming-88a18d9ec7c