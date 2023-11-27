# Inheritance is the concept of having a class inherit from another class because it allows for code to be reused.

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError(
            "Subclasses must implement the 'speak' method")

# Derived class 1


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Derived class 2


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Derived class 3


class Duck(Animal):
    def speak(self):
        return f"{self.name} says Quack!"


# Create instances of the derived classes
dog_instance = Dog("Buddy")
cat_instance = Cat("Whiskers")
duck_instance = Duck("Donald")

# Call the 'speak' method on each instance
print(dog_instance.speak())  # Output: Buddy says Woof!
print(cat_instance.speak())  # Output: Whiskers says Meow!
print(duck_instance.speak())  # Output: Donald says Quack!


# Resources:
# https://medium.com/@rogercodes1/what-is-object-oriented-programming-88a18d9ec7c
