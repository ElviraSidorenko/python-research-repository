# MVC Pattern: Model-View-Controller Pattern
# The Model-View-Controller (MVC) pattern is a design pattern commonly used in software development for separating the concerns of an application into three main components: Model, View, and Controller.


# Model
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

# View


class StudentView:
    def print_student_details(self, student):
        print(f"Student: {student.name}, Roll Number: {student.roll_number}")

# Controller


class StudentController:
    def __init__(self, student, view):
        self.student = student
        self.view = view

    def set_student_name(self, name):
        self.student.name = name

    def get_student_name(self):
        return self.student.name

    def set_student_roll_number(self, roll_number):
        self.student.roll_number = roll_number

    def get_student_roll_number(self):
        return self.student.roll_number

    def update_view(self):
        self.view.print_student_details(self.student)


# Usage
# Create a student
student = Student("John Doe", "12345")

# Create a view
view = StudentView()

# Create a controller
controller = StudentController(student, view)

# Display initial student details
controller.update_view()

# Update student details through the controller
controller.set_student_name("Jane Doe")
controller.set_student_roll_number("54321")

# Display updated student details
controller.update_view()


# In this example:

# Student is the Model, representing the data structure.
# StudentView is the View, responsible for presenting the data to the user.
# StudentController is the Controller, which handles user inputs and updates the model and view accordingly.
