# OCP: Open-Closed Principle
# The Open/Closed Principle indicates that classes should be open for extension, but closed for modification.
# In other words, the code should be written in such a way that, when adding new functionality, previously written code, which may be in use by other users, should not be modified.


# Example without following the Open/Closed Principle

from abc import ABC, abstractmethod


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class AreaCalculator:
    def calculate_area(self, rectangle):
        if isinstance(rectangle, Rectangle):
            return rectangle.width * rectangle.height
        elif isinstance(rectangle, Square):
            return rectangle.side * rectangle.side

# Now, imagine you want to add a new shape, Circle.
# You would need to modify the AreaCalculator class.


class Circle:
    def __init__(self, radius):
        self.radius = radius

# Modified AreaCalculator to include Circle


class AreaCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        elif isinstance(shape, Square):
            return shape.side * shape.side
        elif isinstance(shape, Circle):
            return 3.14 * shape.radius * shape.radius


# Example following the Open/Closed Principle


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class AreaCalculator:
    def calculate_area(self, shape):
        return shape.area()

# Now, if you want to add a new shape, you can create a new class that inherits from the Shape abstract class and implement the area method without modifying the AreaCalculator class.
# This adheres to the Open/Closed Principle.
