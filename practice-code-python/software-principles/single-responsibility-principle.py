# SRP: Single Responsibility Principle
# The first principle of SOLID called the Single Responsibility Principle states that a class should be responsible for only one functionality.
# In other words, the class should only have a single reason to change.

# In the following simple example a Duck class with 5 different methods is defined:

class Duck:

    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"

    def greet(self, duck2: Duck):
        print(f"{self.name}: {self.do_sound()}, hello {duck2.name}")

# The main functionality of this class is to define a duck.
# If this definition needs to be changed, this class will be changed.
# The problem lies in the greet() method, which is responsible for being able to talk to other ducks.
# If you wanted to change the functionality of the conversation between ducks, you would be changing the Duck class as well, i.e., there would be an additional reason to change the class.
# The consequences of not respecting this principle may be several, such as making error debugging more difficult, since several errors point to the same place and the functionalities are more closely coupled.


# To solve this problem in the case of the example, a new Communicator class is defined that takes care of all the communication functionality.
# This new class allows a conversation between two ducks, where they greet each other.
# In this way, the communication functionality has been changed without affecting the Duck class.

class Duck:

    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"


class Communicator:

    def __init__(self, channel):
        self.channel = channel

    def communicate(self, duck1: Duck, duck2: Duck):
        sentence1 = f"{duck1.name}: {duck1.do_sound()}, hello {duck2.name}"
        sentence2 = f"{duck2.name}: {duck2.do_sound()}, hello {duck1.name}"
        conversation = [sentence1, sentence2]
        print(*conversation,
              f"(via {self.channel})",
              sep='\n')


# Resources:
# https://blog.damavis.com/en/solid-principles-illustrated-in-simple-python-examples/
