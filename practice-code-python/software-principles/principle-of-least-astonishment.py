# PoLA: Principle of Least Astonishment (aka Principle of Least Surprise)
# The principle proposes that a component of a system should behave in a way that most users will expect it to behave, and therefore not astonish or surprise users.

# In Python, one example of this principle is related to the use of mutable default arguments in function definitions.

def add_item(item, items=[]):
    items.append(item)
    return items

# At first glance, you might expect that calling this function multiple times with different items would create a list of items.
# However, due to the mutable default argument, unexpected behavior can occur:


# Example 1
result1 = add_item(1)
print(result1)  # Output: [1]

# Example 2
result2 = add_item(2)
print(result2)  # Output: [1, 2] (surprising!)

# In the second example, you might expect result2 to be [2], but it includes the item from the first call as well.
# This is because the default argument items=[] is only created once when the function is defined, and subsequent calls modify the same list.


# To adhere to the principle of least astonishment, you can use None as a default value and create a new list inside the function:
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


# Now, the function behaves more predictably:
result1 = add_item(1)
print(result1)  # Output: [1]

result2 = add_item(2)
print(result2)  # Output: [2] (as expected)


# Resources:
# https://en.wikipedia.org/wiki/Principle_of_least_astonishment#:~:text=In%20user%20interface%20design%20and,not%20astonish%20or%20surprise%20users.
# https://learning.oreilly.com/library/view/learn-python-programming/9781788996662/45238cc9-64ec-400b-9939-efbdc517fe91.xhtml
# https://www.pentalog.com/blog/it-development-technology/software-design-principles/
