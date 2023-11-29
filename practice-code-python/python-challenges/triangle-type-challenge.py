# Challenge: Write a Python program that determines and classifies the type of a triangle based on the lengths of its three sides.

# equilateral = 3 equal sides
# isosceles = only 2 equal sides
# scalene = no equal sides


# get the length of all 3 sides
a = int(input('Type length of side one: '))
b = int(input('Type length of side two: '))
c = int(input('Type length of side three: '))


# get the type based on the inputs
def get_type(a, b, c):
    if a == b and b == c:
        type = 'equilateral'
    elif a == b or a == c or b == c:
        type = 'isosceles'
    else:
        type = 'scalene'
    return f"Your triangle is {type}"


# display result
print(get_type(a, b, c))
