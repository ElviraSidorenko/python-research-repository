# Principle: Avoid duplicating code. Encourage code reuse to reduce redundancy.

# Bad Example
def add_numbers(a, b):
    print(a + b)


def subtract_numbers(a, b):
    print(a - b)

# Good Example


def perform_operation(a, b, operation):
    if operation == 'add':
        print(a + b)
    elif operation == 'subtract':
        print(a - b)
