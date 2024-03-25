#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """Initialize the CashRegister object.

        Args:
            discount (float, optional): Discount percentage. Defaults to 0.
        """
        self.items = []       # List to store the names of items
        self.prices = []      # List to store the prices of items
        self.quantities = []  # List to store the quantities of items
        self.total = 0        # Total price of all items
        self.discount = discount  # Discount percentage

    def add_item(self, item, price, quantity=1):
        """Add an item to the cash register.

        Args:
            item (str): Name of the item.
            price (float): Price of the item.
            quantity (int, optional): Quantity of the item. Defaults to 1.
        """
        self.items.append(item)             # Add item name to items list
        self.prices.append(price)           # Add item price to prices list
        self.quantities.append(quantity)    # Add item quantity to quantities list
        self.total += price * quantity      # Update total price

    def apply_discount(self):
        """Apply discount to the total price."""
        if self.discount > 0:
            self.total *= (100 - self.discount) / 100  # Calculate discounted total
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Void the last transaction."""
        if self.items:
            last_price = self.prices.pop()             # Remove last item's price
            last_quantity = self.quantities.pop()      # Remove last item's quantity
            self.total -= last_price * last_quantity  # Subtract last transaction from total
            self.items.pop()                           # Remove last item name from items list

    def reset_register_totals(self):
        """Reset all register totals."""
        self.items = []       # Reset items list
        self.prices = []      # Reset prices list
        self.quantities = []  # Reset quantities list
        self.total = 0        # Reset total price
