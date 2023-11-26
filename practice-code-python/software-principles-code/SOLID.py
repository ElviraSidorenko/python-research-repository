# SOLID:
# 1. Single responsibility principle
# 2. Open closed principle
# 3. Liskov’s substitution principle
# 4. Interface segregation principle
# 5. Dependency inversion principle

# These principles help in designing maintainable and scalable software.

# 1. Single Responsibility Principle (SRP)
# Principle: A class should have only one reason to change.

# Bad Example
from abc import ABC, abstractmethod


class User:
    def calculate_salary(self):
        # Performs salary calculation, violating SRP
        pass

    def generate_report(self):
        # Generates a report, violating SRP
        pass

# Good Example


class User:
    def calculate_salary(self):
        # Performs salary calculation, adhering to SRP
        pass


class ReportGenerator:
    def generate_report(self):
        # Generates a report, adhering to SRP
        pass

# 2. Open/Closed Principle (OCP)
# Principle: Software entities should be open for extension but closed for modification.

# Bad Example


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class AreaCalculator:
    def calculate_area(self, rectangle):
        # Violates OCP, as new shapes require modification of this class
        return rectangle.width * rectangle.height

# Good Example


class Shape:
    def calculate_area(self):
        # Base class for shapes, adhering to OCP
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        # Adheres to OCP by extending Shape without modifying it
        return self.width * self.height


# 3. Liskov Substitution Principle (LSP):
# Principle: Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.

# Bad Example
class Bird:
    def fly(self):
        # Superclass assumes all birds can fly
        pass


class Ostrich(Bird):
    def fly(self):
        # Violates LSP, as ostriches can't fly
        raise NotImplementedError("Ostriches can't fly!")

# Good Example


class Bird:
    def move(self):
        # Revised superclass with a generic move method
        pass


class Ostrich(Bird):
    def move(self):
        # Adheres to LSP by providing a different implementation for movement
        print("Ostrich is running.")


# 4. Interface Segregation Principle (ISP):
# Principle: A class should not be forced to implement interfaces it does not use.

# Bad Example
class Worker:
    def work(self):
        # Worker has to implement unnecessary methods
        pass

    def eat(self):
        # Worker has to implement unnecessary methods
        pass

# Good Example


class Workable:
    def work(self):
        # Interface for work-related behavior
        pass


class Eatable:
    def eat(self):
        # Interface for eating-related behavior
        pass


class Worker(Workable, Eatable):
    # Adheres to ISP by implementing only necessary interfaces
    pass


# 5. Dependency Inversion Principle (DIP)
# Principle: High-level modules should not depend on low-level modules. Both should depend on abstractions.
# Abstractions should not depend on details. Details should depend on abstractions.

# Bad Example
class LightBulb:
    def turn_on(self):
        print("Light bulb is on")


class Switch:
    def __init__(self, bulb):
        self.bulb = bulb

    def operate(self):
        self.bulb.turn_on()

# In this example, Switch depends directly on the concrete implementation (LightBulb).
# If we introduce a new type of bulb, Switch needs to be modified.


# Good Example


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("Light bulb is on")


class Fan(Switchable):
    def turn_on(self):
        print("Fan is spinning")


class Switch:
    def __init__(self, device):
        self.device = device

    def operate(self):
        self.device.turn_on()

# In this improved example, Switch depends on the abstraction (Switchable).
# LightBulb and Fan both implement the Switchable interface.
# If we introduce a new device, we only need to create a new class implementing Switchable.
