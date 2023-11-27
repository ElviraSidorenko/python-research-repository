# Encapsulation is the process of combining data and functions into a single unit called a class; it keeps data both safe from outside interference and misuse.
# With Encapsulation, the data is not accessed directly.
# It can only be accessed through public functions present inside the class called methods.
# Encapsulation is achieved by keeping it’s state private.

# Encapsulation allows for us to create methods that can only be accessed or changed by public methods.


class Car:
    def __init__(self, make, model, year):
        self.__make = make   # private attribute
        self.__model = model  # private attribute
        self.__year = year    # private attribute
        self.__mileage = 0    # private attribute

    # Getter methods to access private attributes
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_mileage(self):
        return self.__mileage

    # Setter method to modify private attribute
    def update_mileage(self, miles):
        if miles >= 0:
            self.__mileage += miles
        else:
            print("Miles cannot be negative.")


# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2020)

# Accessing attributes using getter methods
print("Make:", my_car.get_make())
print("Model:", my_car.get_model())
print("Year:", my_car.get_year())
print("Mileage:", my_car.get_mileage())

# Update mileage using the setter method
my_car.update_mileage(100)
print("Updated Mileage:", my_car.get_mileage())

# Attempting to access private attributes directly will result in an error
# Uncommenting the line below will raise an AttributeError
# print(my_car.__make)

# Resources:
# https://medium.com/@rogercodes1/what-is-object-oriented-programming-88a18d9ec7c
