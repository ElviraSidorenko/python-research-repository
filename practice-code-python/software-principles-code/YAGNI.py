# YAGNI: You Ain't Gonna Need It
# Principle: Only implement functionality when you need it, not when you foresee that you might need it.


# Example Task: Create ShoppingCart class to add products to the cart

# Bad Example
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        # Unnecessary feature for tracking item quantities
        item_quantity = 1
        self.items.append({'item': item, 'quantity': item_quantity})

    def remove_item(self, item):
        # Unnecessary feature for removing items
        self.items = [i for i in self.items if i['item'] != item]

# Good Example
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        # Keep it simple by only adding items to the cart
        self.items.append(item)

# Client code
cart = ShoppingCart()
cart.add_item('Product A')
cart.add_item('Product B')
print(cart.items)  # ['Product A', 'Product B']