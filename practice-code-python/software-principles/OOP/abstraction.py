# The main purpose of Abstraction is to handle the complexity of the program by hiding unnecessary detail from the user.
# This allows users to implement advance logic without having to understand or to think about all the hidden complexity.

from abc import ABC, abstractmethod

# Abstract class (cannot be instantiated directly)


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class implementing the abstract class


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Concrete class implementing the abstract class


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Function that uses the abstraction to calculate area and perimeter


def print_shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
    print()


# Instantiate objects of the concrete classes
circle = Circle(5)
square = Square(4)

# Use the abstraction to calculate and print information about each shape
print("Circle Information:")
print_shape_info(circle)

print("Square Information:")
print_shape_info(square)


# Resources:
# https://medium.com/@rogercodes1/what-is-object-oriented-programming-88a18d9ec7c
