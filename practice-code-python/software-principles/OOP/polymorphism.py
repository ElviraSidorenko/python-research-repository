# Polymorphism is a concept in object-oriented programming (OOP) that allows objects of different types to be treated as objects of a common type.
# It provides a way for objects to be used interchangeably based on a common interface or base class.

# There are two types of polymorphism: compile-time (or static) polymorphism and runtime (or dynamic) polymorphism.
# In Python, we often focus on runtime polymorphism, which is achieved through method overriding.


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # This method will be overridden in the subclasses


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


class Duck(Animal):
    def speak(self):
        return f"{self.name} says Quack!"

# Function demonstrating polymorphism


def animal_sound(animal_instance):
    return animal_instance.speak()


# Create instances of the derived classes
dog_instance = Dog("Buddy")
cat_instance = Cat("Whiskers")
duck_instance = Duck("Donald")

# Use the function with different instances
print(animal_sound(dog_instance))  # Output: Buddy says Woof!
print(animal_sound(cat_instance))  # Output: Whiskers says Meow!
print(animal_sound(duck_instance))  # Output: Donald says Quack!

# In this example:

# The Animal class has a method called speak, which is marked as abstract with a pass statement. Subclasses are expected to override this method.

# The Dog, Cat, and Duck classes are derived classes that override the speak method from the Animal class.

# The animal_sound function takes an object of type Animal (or any of its subclasses) and calls the speak method on it. This function can work with different types of animals without knowing their specific class.


# Resources:
# https://medium.com/@rogercodes1/what-is-object-oriented-programming-88a18d9ec7c
