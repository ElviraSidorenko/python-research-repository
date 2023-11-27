# DIP: Dependancy Inversion Principle
# The Principle of Dependency Inversion can be separated into two statements.
# On the one hand, it indicates that abstractions should not depend on details, since details should depend on abstractions.
# On the other hand, it indicates that high-level classes should not depend on low-level classes, since both should depend on abstractions.
# In summary, abstractions should depend on abstractions.
# The dependency inversion principle aims to reduce the coupling between classes by creating an abstraction layer between them.

# Bad example

from abc import ABC


class FXConverter:
    def convert(self, from_currency, to_currency, amount):
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2


class App:
    def start(self):
        converter = FXConverter()
        converter.convert('EUR', 'USD', 100)


if __name__ == '__main__':
    app = App()
    app.start()

# The App class is a high-level module. However, The App depends heavily on the FXConverter class that is dependent on the FX’s API.
# In the future, if the FX’s API changes, it’ll break the code. Also, if you want to use a different API, you’ll need to change the App class.

# To prevent this, you need to invert the dependency so that the FXConverter class needs to adapt to the App class.
# To do that, you define an interface and make the App dependent on it instead of FXConverter class. And then you change the FXConverter to comply with the interface.


# Define an abstract class CurrencyConverter that acts as an interface.
class CurrencyConverter(ABC):
    def convert(self, from_currency, to_currency, amount) -> float:
        pass


# Redefine the FXConverter class so that it inherits from the CurrencyConverter class and implement the convert() method:
class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using FX API')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 2


# Add the __init__ method to the App class and initialize the CurrencyConverter‘s object:
class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        self.converter.convert('EUR', 'USD', 100)


# Now, the App class depends on the CurrencyConverter interface, not the FXConverter class.
# In the future, we can support another currency converter API by subclassing the CurrencyConverter class.

# Use the dependency inversion principle to make your code more robust by making the high-level module dependent on the abstraction, not the concrete implementation.

# Resources:
# https://blog.damavis.com/en/solid-principles-illustrated-in-simple-python-examples/
# https://www.pythontutorial.net/python-oop/python-dependency-inversion-principle/
