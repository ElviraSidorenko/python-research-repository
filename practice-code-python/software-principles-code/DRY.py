
# DRY: Don't Repeat Yourself
# Principle: Avoid duplicating code. Encourage code reuse to reduce redundancy.

# Bad Example
def add_numbers(a, b):
    # Duplicated logic for addition
    print(a + b)


def subtract_numbers(a, b):
    # Duplicated logic for subtraction
    print(a - b)


# Good Example
def perform_operation(a, b, operation):
    # Reusable function for performing various operations
    if operation == 'add':
        print(a + b)
    elif operation == 'subtract':
        print(a - b)