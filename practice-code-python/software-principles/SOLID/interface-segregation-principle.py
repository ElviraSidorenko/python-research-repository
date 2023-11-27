# ISP: Interface Segregation Principle
# The Interface Segregation Principle states that clients should not be forced to rely on methods they do not use and therefore suggests the creation of specific interfaces or classes for such clients.
# An interface is a description of behaviors that an object can do.
# In object-oriented programming, an interface is a set of methods an object must-have.
# The purpose of interfaces is to allow clients to request the correct methods of an object via its interface.
# The interface segregation principle states that an interface should be as small a possible in terms of cohesion. In other words, it should do ONE thing.
# It doesn’t mean that the interface should have one method. An interface can have multiple cohesive methods.

from abc import ABC, abstractmethod


# Define a Vehicle abstract class that has two abstract methods, go() and fly():
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def fly(self):
        pass


# Define the Aircraft class that inherits from the Vehicle class and implement both go() and fly() methods:
class Aircraft(Vehicle):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")


# Define the Car class that inherits from the Vehicle class. Since a car cannot fly, we raise an exception in the fly() method:
class Car(Vehicle):
    def go(self):
        print("Going")

    def fly(self):
        raise Exception('The car cannot fly')

# In this design the Car class must implement the fly() method from the Vehicle class that the Car class doesn’t use.
# Therefore, this design violates the interface segregation principle.

# To fix this, we need to split the Vehicle class into small ones and inherits from these classes from the Aircraft and Car classes.

# Split the Vehicle interface into two smaller interfaces: Movable and Flyable, and inherits the Movable class from the Flyable class:


class Movable(ABC):
    @abstractmethod
    def go(self):
        pass


class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass

# Inherit the Flyable class from the Aircraft class:


class Aircraft(Flyable):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")

# Inherit the Movable class from the Car class:


class Car(Movable):
    def go(self):
        print("Going")

# In this design, the Car only need to implement the go() method that it needs. It doesn’t need to implement the fly() method that it doesn’t use.

# Resources:
# https://blog.damavis.com/en/solid-principles-illustrated-in-simple-python-examples/
# https://www.pythontutorial.net/python-oop/python-interface-segregation-principle/
