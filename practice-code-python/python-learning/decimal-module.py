# Import module
from decimal import Decimal, getcontext

print(getcontext())  # Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])

# Set the precision to 4 digits
getcontext().prec = 4

print(getcontext())  # Context(prec=4, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])

# Create Decimal objects
a = Decimal('1.234')
b = Decimal('2.345')

# Perform arithmetic operations
sum_result = a + b
product_result = a * b

# Display results
print(f"Sum: {sum_result}")
print(f"Product: {product_result}")
