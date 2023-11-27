# Decorator functions are useful to make DRY code which avoids code repetition. They are used in cases where the same logic needs to be applied to multiple functions. Because the *args and **kwargs types are used, we do not restrict ourselves to functions that have only one, two or three arguments. We can decorate a function with any number of arguments.

# Put the error checking logic into the decorator function
def decorator(fun):
    def wrapper(*args, **kwargs):

        nums = args[:-1]
        for arg in nums:
            try:
                int(arg)
            except ValueError:
                return {'message': 'Invalid input'}

        tu = tuple(map(int, nums))
        tu = tu + (args[-1],)
        return fun(*tu, **kwargs)

    return wrapper

# If we use the @ notation before a function definition, the decorator function will wrap around the function being defined.


@decorator
def simpleMath(num1, num2, operator):

    if operator == '+':
        return {"result": num1 + num2}
    elif operator == '-':
        return {"result": num1 - num2}
    elif operator == '*':
        return {"result": num1 * num2}
    elif operator == '/':
        return {"result": num1 / num2}

# The same logic can be applied to the another function.


@decorator
def complexMath(num1, num2, num3, operator):

    if operator == '+':
        return {"result": num1 + num2 + num3}
    elif operator == '-':
        return {"result": num1 - num2 - num3}
    elif operator == '*':
        return {"result": num1 * num2 * num3}
    elif operator == '/':
        return {"result": num1 / num2 / num3}

# Decorator function can be used for as many functions instead of adding its logic inside each individual function.