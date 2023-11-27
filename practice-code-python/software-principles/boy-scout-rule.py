# Boy Scout Rule
# Leave your code better than you found it.
# "The act of leaving a mess in the code should be as socially unacceptable as littering." -- Robert C. "Uncle Bob" Martin


# Original code example:
def fact(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result = result * i
        return result


# Example usage
result = fact(5)
print(result)


# In this bad code example:

# The function name fact is not descriptive.
# The loop variable i is not descriptive.
# The variable result is used for both the initial value and the final result, which can be confusing.

# Good Code (After Applying Boy Scout Rule):

def factorial(n):
    if n == 0:
        return 1
    else:
        product = 1
        for num in range(1, n + 1):
            product *= num
        return product


# Example usage
result = factorial(5)
print(result)

# In the improved code:

# The function name is changed to factorial for better clarity.
# The loop variable i is renamed to num for better readability.
# The variable result is renamed to product to better reflect its purpose.

# Resources:
# https://deviq.com/principles/boy-scout-rule
# https://accesto.com/blog/Boy-scout-rule-in-6-examples-the-basic-principle-of-web-development/
