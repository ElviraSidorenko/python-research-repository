# In Python, a class is a blueprint or a template for creating objects.
# It defines the attributes (data) and methods (functions) that the objects created from the class will have.

class MyClass:
    # Class-level attribute (shared by all instances)
    class_attribute = "I am a class attribute"

    # Constructor method (initialize object attributes)
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    # Instance method
    def instance_method(self):
        return f"Instance method called with attributes: {self.attribute1}, {self.attribute2}"


# Creating instances of the class
object1 = MyClass("Value 1", "Value 2")
object2 = MyClass("Another Value", "Yet Another Value")

# Accessing class attributes and calling instance methods
print(object1.class_attribute)  # Accessing a class attribute
print(object2.instance_method())  # Calling an instance method
