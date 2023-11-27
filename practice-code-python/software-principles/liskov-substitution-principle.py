# LSP: Liskov Substitution Principle
# Liskov’s Principle of Substitution states that classes should be substitutable by instances of their subclasses.

class Bird:
    def fly(self):
        pass


class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")


class Penguin(Bird):
    def fly(self):
        print("Penguin can't fly")


def make_bird_fly(bird):
    bird.fly()


# Using LSP
sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow)  # Output: Sparrow is flying
make_bird_fly(penguin)  # Output: Penguin can't fly


# In this example, we have a base class Bird with a method fly.
# The subclasses Sparrow and Penguin inherit from the Bird class and provide their own implementations of the fly method.
# The make_bird_fly function takes any object of type Bird and calls its fly method.
# The key here is that both Sparrow and Penguin are subclasses of Bird, and they can be used interchangeably in the make_bird_fly function without affecting the correctness of the program.
# This adheres to the Liskov Substitution Principle.
# If the LSP is violated, replacing an object of the base class with an object of the subclass could lead to unexpected behavior or errors in the program.
